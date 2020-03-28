from django.db import models


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        """Return string representation of Users"""
        return self.name

    class Meta:
        ordering = ["created_at"]


class Profile(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user_id = models.BigIntegerField()
    image = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    current_school = models.CharField(max_length=255, blank=True, null=True)
    gpa = models.CharField(max_length=255, blank=True, null=True)
    major = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.CharField(max_length=255, blank=True, null=True)
    citizenship = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    disabilities = models.CharField(max_length=255, blank=True, null=True)
    ethnicity = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    sports = models.CharField(max_length=255, blank=True, null=True)
    fraternity = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        """Return string representation of profile"""
        return self.id

    class Meta:
        ordering = ["created_at"]


class Post(models.Model):
    """Database model for users in the system"""
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    post_title = models.CharField(max_length=255)
    user_id = models.BigIntegerField()
    post_category = models.CharField(max_length=255, blank=True, null=True)
    post_content = models.CharField(max_length=255)
    post_comment_count = models.CharField(max_length=255)
    post_view_count = models.CharField(max_length=255)
    post_likes = models.CharField(max_length=255)
    post_dislikes = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of post"""
        return self.post_title

    class Meta:
        ordering = ["created_at"]


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user_id = models.BigIntegerField()
    comment_post_id = models.BigIntegerField()
    comment_author = models.CharField(max_length=255)
    comment_content = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of comments"""
        return self.comment_post_id

    class Meta:
        ordering = ["created_at"]
