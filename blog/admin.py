from django.contrib import admin
from django.utils.translation import gettext as _

from django.contrib.auth import get_user_model

from django_summernote.admin import SummernoteModelAdmin

from blog import models



User = get_user_model()


class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "email", 
        "text_excerpt",
        "post",
        
        "created_at",
        "updated_at",
        "published"
    ]

    list_display_links = [
        "id",
        "email"
    ]

    list_filter = [
        "created_at",
        "updated_at",
        "email",
        "published",
        "post"
    ]

    search_fields = [
        "email",
        "text"
    ]

    list_editable = [
        "published"
    ]


class CommentInline(admin.StackedInline):
    model = models.Comment
    extra = 0

    fields = [
        "email",
        "text",
        "created_at",
        "updated_at",
        "published",
    ]

    readonly_fields = [
        "created_at",
        "updated_at"
    ]



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

    list_filter = [
        "created_at",
        "updated_at"
    ]

    search_fields = [
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

    list_filter = [
        "created_at",
        "updated_at"
    ]

    search_fields = [
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
        "featured",
        "allow_comments",
        "show_comments",
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
        "published"
    ]

    list_filter = [
        "created_at",
        "updated_at",
        "user",
        "tags",
        "featured",
        "allow_comments",
        "show_comments",
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
        "excerpt",
        "featured",
        "allow_comments",
        "show_comments",
        "published"
    ]

    

    raw_id_fields = [
        "post_image"
    ]


    inlines = [
        CommentInline
    ]


    # actions
    actions = [
        "set_to_published",
        "set_to_draft",

        "make_featured",
        "make_disfeatured",

        "allow_comments",
        "disallow_comments",

        "show_comments",
        "hide_comments"

    ]

    @admin.display(description=_("Publish selected Post"))
    def set_to_published(self, request, queryset):
        count = queryset.update(published=True)
        self.message_user(request, f"{count} Posts have been published.")
    
    

    @admin.display(description=_("Unpublish selected Post"))
    def set_to_draft(self, request, queryset):
        count = queryset.update(published=False)
        self.message_user(request, f"{count} Posts have been setted to drafts.")

    #set_to_draft.short_description = "Set Post to draft"


    @admin.display(description=_("Featured selected Post"))
    def make_featured(self, request, queryset):
        count = queryset.update(featured=True)
        self.message_user(request, f"{count} Posts have been made featured.")


    @admin.display(description=_("Disfeatured selected Post"))
    def make_disfeatured(self, request, queryset):
        count = queryset.update(featured=False)
        self.message_user(request, f"{count} Posts have been made undo featured.")


    @admin.display(description=_("Allow comments at selected Post"))
    def allow_comments(self, request, queryset):
        count = queryset.update(allow_comments=True)
        self.message_user(request, f"{count} Posts have been made to allow comments.")


    @admin.display(description=_("Disallow comments at selected Post"))
    def disallow_comments(self, request, queryset):
        count = queryset.update(allow_comments=False)
        self.message_user(request, f"{count} Posts have been made to disallow comments.")


    @admin.display(description=_("Show comments at selected Post"))
    def show_comments(self, request, queryset):
        count = queryset.update(show_comments=True)
        self.message_user(request, f"{count} Posts have been shown comments.")

    @admin.display(description=_("Hide comments at selected Post"))
    def hide_comments(self, request, queryset):
        count = queryset.update(show_comments=False)
        self.message_user(request, f"{count} Posts have been hidden comments.")







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
    

    # remove the user field of the filterlist
    def get_list_filter(self, request):
        lf = super().get_list_filter(request)
        print(lf)
        if request.user.is_superuser:
            return lf
        else:
            # print(lf)
            new_lf = [item for item in lf if item != "user"]
            return new_lf




admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.PostImage, PostImageAdmin)
admin.site.register(models.Post, PostAdmin)
