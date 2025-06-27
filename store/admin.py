from django.contrib import admin

from .models import Category, Furniture, Project, ProjectItem, ProjectItemImage, FurnitureImage


class FurnitureImageInline(admin.TabularInline):
    model = FurnitureImage
    extra = 1
    max_num = 10
    fields = ['image', 'alt_text']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Furniture)
class FurnitureAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    inlines = [FurnitureImageInline]


class ProjectItemImageInline(admin.TabularInline):
    model = ProjectItemImage
    extra = 1
    max_num = 10
    fields = ['image', 'alt_text']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

@admin.register(ProjectItem)
class ProjectItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ['name', 'project']
    inlines = [ProjectItemImageInline]