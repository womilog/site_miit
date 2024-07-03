from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .models import Prepod, PrepodCategory

admin.site.register(Prepod)
admin.site.register(PrepodCategory)


# @admin.register(Prepod)
# class PrepodAdmin(admin.ModelAdmin):
#     fields = ['name', 'slug', 'age', 'nickname', 'content', 'photo', 'post_photo', 'cat', 'husband', 'tags']
#     readonly_fields = ['post_photo']
#     prepopulated_fields = {"slug": ("name", )}
#     list_display = ('name', 'post_photo', 'time_create', 'is_published', 'cat')
#     list_display_links = ('name', )
#     ordering = ['-time_create', 'name']
#     list_editable = ('is_published', )
#     actions = ['set_published', 'set_draft']
#     search_fields = ['cat__name']
#     list_filter = ['cat__name', 'is_published']
#     save_on_top = True
#
#     @admin.display(description="Изображение", ordering='content')
#     def post_photo(self, prepod: Prepod):
#         if prepod.photo:
#             return mark_safe(f"<img src='{prepod.photo.url}' width=50>")
#         return "Без фото"
#
#     @admin.action(description="Опубликовать выбранные записи")
#     def set_published(self, request, queryset):
#         count = queryset.update(is_published=Prepod.Status.PUBLISHED)
#         self.message_user(request, f"Изменено {count} записей.")
#
#     @admin.action(description="Снять с публикации выбранные записи")
#     def set_draft(self, request, queryset):
#         count = queryset.update(is_published=Prepod.Status.DRAFT)
#         self.message_user(request, f"{count} записей сняты с публикации!", messages.WARNING)
#
#
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     list_display_links = ('id', 'name')
