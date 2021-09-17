# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class food_diary(models.Model):
    mfg_code = models.CharField(max_length=10, blank=True, null=True)
    food_id = models.CharField(max_length=10, blank=True, null=True)
    food_name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    food_type = models.CharField(max_length=200, blank=True, null=True)
    calories = models.CharField(max_length=10, blank=True, null=True)
    fats = models.CharField(max_length=10, blank=True, null=True)
    protein = models.CharField(max_length=10, blank=True, null=True)
    carbohydrates = models.CharField(max_length=10, blank=True, null=True)
    link_of_image = models.CharField(max_length=1000, blank=True, null=True)
    link_of_recipie = models.CharField(max_length=1000, blank=True, null=True)
    purchasing_link = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basic_app_food_diary'
