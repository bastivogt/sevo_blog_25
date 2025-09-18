from django.contrib import admin

from django.contrib.auth import get_user_model

from django_summernote.admin import SummernoteModelAdmin

from blog import models



User = get_user_model()

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


class PostAdmin(SummernoteModelAdmin):

    summernote_fields = [
        'content'
    ]
    # list_per_page = 50

    list_display = [
        "get_image_tag",
        "id", 
        "title",
        "published",
        "created_at",
        "updated_at"
    ]

    list_display_links = [
        "get_image_tag",
        "id", 
        "title"
    ]

    list_editable = [
        #"published"
    ]

    list_filter = [
        "created_at",
        "updated_at",
        "user",
        "tags",
        "published"
    ]


    search_fields = [
        "title",
        "content"
    ]

    readonly_fields = [
        "get_image_tag",
        "get_image_tag_link",
        "get_image_url",
        "get_image_link"
    ]

    fields = [
        "user",
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


    # actions
    actions = [
        "set_to_published",
        "set_to_draft"
    ]

    @admin.display(description="Publish selected Post")
    def set_to_published(self, request, queryset):
        count = queryset.update(published=True)
        self.message_user(request, f"{count} Posts have been published.")
    
    

    @admin.display(description="Unpublish selected Post")
    def set_to_draft(self, request, queryset):
        count = queryset.update(published=False)
        self.message_user(request, f"{count} Posts have been setted to drafts.")

    #set_to_draft.short_description = "Set Post to draft"







    # listview
    def get_queryset(self, request):
        q = super().get_queryset(request)
        if request.user.is_superuser:
            return q
        else:
            logged_user = request.user
            return q.filter(user=logged_user)


    # formfield
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser:
            if db_field.name == "user":
                kwargs["queryset"] = get_user_model().objects.filter(
                    username=request.user.username
                )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            if obj is not None:
                return self.readonly_fields + ["user"]
        return self.readonly_fields

    def add_view(self, request, form_url="", extra_context=None):
        data = request.GET.copy()
        data["user"] = request.user
        request.GET = data
        return super().add_view(
            request, form_url="", extra_context=extra_context
        )
    

    # remove the user of the filterlist
    def get_list_filter(self, request):
        lf = super().get_list_filter(request)
        print(lf)
        if request.user.is_superuser:
            return lf
        else:
            # print(lf)
            new_lf = [item for item in lf if item != "user"]
            return new_lf




admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.PostImage, PostImageAdmin)
admin.site.register(models.Post, PostAdmin)
