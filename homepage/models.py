from djongo import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=255, null=False,
                            blank=False, unique=True)

    def __str__(self):
        return f'{self.name}'


class Author(models.Model):
    name = models.CharField(max_length=255, null=False,
                            blank=False, unique=True)

    def __str__(self):
        return f'{self.name}'


class Publisher(models.Model):
    name = models.CharField(max_length=255, null=False,
                            blank=False, unique=True)

    def __str__(self):
        return f'{self.name}'


class Content(models.Model):
    # Constant for Status
    DRAFT = "DRAFT"
    POSTED = "POSTED"
    DELETED = "DELETED"
    STATUS_CHOICE = (
        (DRAFT, "Draft"),
        (POSTED, "Posted"),
        (DELETED, "Deleted"),
    )

    # Constant for content types
    CENSORED = "CENSORED"
    UNCENSORED = "UNCENSORED"
    TYPE_CHOICE = (
        (CENSORED, "Censored"),
        (UNCENSORED, "Uncensored"),
    )

    # Fields
    slug = models.SlugField(max_length=255,
                            unique=True, null=False,
                            blank=False,)

    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(null=False, blank=False,)
    content = models.FileField(blank=True, null=True, default=None)
    description = models.TextField(null=False, blank=False, default="Udating")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    publication_date = models.IntegerField(default="2022",
                                           null=False,
                                           blank=False,
                                           validators=[MaxValueValidator(2022), MinValueValidator(1900)])

    active = models.BooleanField(default=True)

    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICE,
                              null=True)
    # Foreign Field
    authors = models.ManyToManyField(Author,
                                    related_name="contents", blank=False,)
    publishers = models.ManyToManyField(Publisher,
                                       related_name="contents", blank=False,)
    categories = models.ManyToManyField(Category, related_name="contents", blank=False,)
    # Embedded Field
    # comments = models.EmbeddedField(model_container="Comment")

    def __str__(self):
        return f"{ self.author } | { self.title }"

    # def get_absolute_url(self):
    #     return reverse('content-detail-slug', kwargs={"slug", self.slug })


class ContentSeries(models.Model):
    name = models.CharField(max_length=255)
    contents = models.ManyToManyField(Content, related_name="contents")
