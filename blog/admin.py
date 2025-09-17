from django.contrib import admin

from blog import models

class TagAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "created_at",
        "updated_at"
    ]

    list_display_links = [
        "id",
        "title"
    ]

class PostImageAdmin(admin.ModelAdmin):
    list_display = [
        "get_image_tag",
        "id",
        "title",
        "created_at",
        "updated_at"
    ]

    list_display_links = [
        "get_image_tag",
        "id",
        "title"
    ]


class PostAdmin(admin.ModelAdmin):
    list_display = [
        "get_image_tag",
        "id", 
        "title",
        "created_at",
        "updated_at"
    ]

    list_display_links = [
        "get_image_tag",
        "id", 
        "title"
    ]

    readonly_fields = [
        "get_image_tag",
        "get_image_tag_link",
        "get_image_url",
        "get_image_link"
    ]

    fields = [
        "title",
        "tags",
        "post_image",
        "get_image_tag_link",
        "get_image_link",
        "content",
        "published"
    ]

    raw_id_fields = [
        "post_image"
    ]


admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.PostImage, PostImageAdmin)
admin.site.register(models.Post, PostAdmin)
