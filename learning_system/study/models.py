from django.db import models, transaction
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import F
from django.utils import timezone

from catalog.models import Product, ProductAccess


class Lesson(models.Model):
    title = models.CharField(max_length=32)
    video_url = models.URLField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Group(models.Model):
    title = models.CharField(max_length=32)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    students = models.ManyToManyField(User)


@receiver(post_save, sender=ProductAccess)
def handle_product_access(sender, instance, created, **kwargs):
    if created and instance.is_valid:
        if instance.product.datetime_start <= timezone.now():
            distribute_user_to_group(instance.product, instance.user)
        else:
            instance.is_valid = False
            instance.save()
            rebuild_groups(instance.product)


@transaction.atomic
def distribute_user_to_group(product, user):
    groups = product.group_set.all()

    if not groups.exists():
        # Create a new group and add the user if no groups exist
        new_group = Group.objects.create(product=product, title=f"Group {product.group_set.count() + 1}")
        new_group.students.add(user)
        return

    # Simplify sorting groups by using the 'students' count directly
    sorted_groups = sorted(groups, key=lambda group: group.students.count())
    min_group = sorted_groups[0]

    if min_group.students.count() < product.min_size_group:
        # Rebuild groups if the minimum size is not met
        rebuild_groups(product)
        min_group.students.add(user)
    elif min_group.students.count() > product.max_size_group:
        # Create a new group if the maximum size is exceeded
        new_group = Group.objects.create(product=product, title=f"Group {product.group_set.count() + 1}")
        new_group.students.add(user)
    else:
        min_group.students.add(user)


@transaction.atomic
def rebuild_groups(product):
    desired_group_size = (product.min_size_group + product.max_size_group) // 2
    groups = Group.objects.filter(product=product).prefetch_related('students')

    for group in groups:
        current_group_size = group.students.count()
        difference = desired_group_size - current_group_size

        if difference > 1:
            other_groups = groups.exclude(id=group.id).prefetch_related('students')

            for other_group in other_groups:
                other_group_size = other_group.students.count()
                move_count = min(difference, other_group_size)

                # Use F() expressions for atomic update to move students
                other_group.students.remove(*other_group.students.all()[:move_count])
                Group.objects.filter(id=group.id).update(
                    students=F('students') + other_group.students.all()[:move_count])

                difference -= move_count

                if difference <= 1:
                    break
