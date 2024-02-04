# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AreaData(models.Model):
    area_id = models.IntegerField(primary_key=True)
    area_locations = models.JSONField()
    area_date = models.IntegerField()
    area_info = models.JSONField(blank=True, null=True)
    area_pois = models.JSONField(blank=True, null=True)
    area_extend = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "area_data"


class CommentData(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    owner = models.PositiveIntegerField()
    pois_id = models.PositiveIntegerField()
    root = models.PositiveIntegerField()
    parent = models.PositiveIntegerField()
    commentcontent = models.CharField(
        db_column="commentContent", max_length=255
    )  # Field name made lowercase.
    date = models.PositiveIntegerField()
    commentlevel = models.PositiveIntegerField(
        db_column="commentLevel"
    )  # Field name made lowercase.
    type = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = "comment_data"


class FeedbackData(models.Model):
    feedback_id = models.IntegerField(primary_key=True)
    feedback_info = models.JSONField()
    feedback_type = models.IntegerField()
    feedback_date = models.IntegerField()
    feedback_images = models.JSONField(blank=True, null=True)
    feedback_owenr = models.IntegerField()
    feedback_solution = models.JSONField(blank=True, null=True)
    feedback_solved_date = models.IntegerField(blank=True, null=True)
    feedback_extend = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "feedback_data"


class PoisData(models.Model):
    poi_id = models.IntegerField(primary_key=True)
    poi_info = models.JSONField(blank=True, null=True)
    poi_owenr = models.IntegerField()
    poi_location = models.JSONField()
    poi_date = models.IntegerField()
    poi_star = models.CharField(max_length=255)
    poi_comments = models.JSONField(blank=True, null=True)
    poi_share = models.CharField(max_length=255)
    poi_pv = models.CharField(max_length=255)
    poi_uv = models.CharField(max_length=255)
    poi_images = models.JSONField(blank=True, null=True)
    poi_extend = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "pois_data"


class User(models.Model):
    user_account = models.PositiveIntegerField(primary_key=True, db_comment="用户id")
    user_phone = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255)
    user_account_type = models.IntegerField()
    user_wx_info = models.JSONField(blank=True, null=True)
    user_password = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    user_real_info = models.JSONField(blank=True, null=True)
    user_real_status = models.IntegerField()
    user_qr_code = models.CharField(max_length=255, blank=True, null=True)
    user_privilege = models.IntegerField()
    user_extend = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "user"


class UserData(models.Model):
    user_account = models.IntegerField(primary_key=True, db_comment="用户id")
    user_avatar = models.CharField(max_length=255, blank=True, null=True)
    user_bg = models.CharField(max_length=255, blank=True, null=True)
    user_info = models.JSONField(blank=True, null=True)
    user_pois = models.JSONField(blank=True, null=True)
    user_history = models.JSONField(blank=True, null=True)
    user_footprint = models.JSONField(blank=True, null=True)
    user_favorites = models.JSONField(blank=True, null=True)
    user_follow = models.JSONField(blank=True, null=True)
    user_followed = models.JSONField(blank=True, null=True)
    user_extend = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "user_data"


class UserTag(models.Model):
    tag_id = models.IntegerField(primary_key=True)
    tag_content = models.CharField(max_length=255)
    tag_heat = models.IntegerField()

    class Meta:
        managed = False
        db_table = "user_tag"
