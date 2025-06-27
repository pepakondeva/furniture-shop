from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name_plural = 'projects'

    def __str__(self):
        return self.name


class ProjectItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='images/')

    # FK
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE,
                                null=False)

    class Meta:
        verbose_name_plural = 'Project_Items'

    def __str__(self):
        return self.name


class ProjectItemImage(models.Model):
    project_item = models.ForeignKey(
        ProjectItem,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='images'
    )
    image = models.ImageField(upload_to='images/project_items/')
    alt_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.project_item.name}"


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Furniture(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='images/')

    # FK
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 null=False)

    #  how it will look like in the admin and db
    class Meta:
        verbose_name_plural = 'furnitures'

    def __str__(self):
        return self.name


class FurnitureImage(models.Model):
    furniture_item = models.ForeignKey(
        Furniture,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='furniture_images'
    )
    image = models.ImageField(upload_to='images/furniture_items/')
    alt_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.furniture_item.name}"