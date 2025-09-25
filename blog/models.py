from django.db import models
from django.utils.translation import gettext as _
from django.utils.html import format_html
from django.contrib import admin




from django.contrib.auth import get_user_model
User = get_user_model()


from blog import settings




class Tag(models.Model):
    title = models.CharField(max_length=150, verbose_name=_("Title"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        ordering = [
            "-created_at"
        ]
        verbose_name = _("Tag")


class PostImage(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="uploads/images/blog")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    def __str__(self):
        return f"#{self.id} - {self.title}"
    
    def delete(self, *args, **kwargs):
        self.image.delete()
        return super().delete(*args, **kwargs)
    
    @admin.display(description=_("Image preview"))
    def get_image_tag(self):
        if self.image:
            img_tag = f'<img src="{self.image.url}" title="{self.title}" alt="{self.title}" style="width: 80px; height: 80px; object-fit:cover;" />'
            return format_html(img_tag)
        return None
    
    @admin.display(description=_("Image preview link"))
    def get_image_tag_link(self):
        if self.image:
            a_tag = f'<a href="{self.image.url}" title="{self.title}" target="_blank">{self.get_image_tag()}</a>'
            return format_html(a_tag)
        return None
    
    @admin.display(description=_("Image URL"))
    def get_image_url(self):
        if self.image:
            return self.image.url
        return None
    
    @admin.display(description=_("Image link"))
    def get_image_link(self):
        if self.image:
            a_tag = f'<a href="{self.image.url}" title="{self.title}" target="_blank">{self.image.url}</a>'
            return format_html(a_tag)
        return None
    
    class Meta:
        ordering = [
            "-created_at"
        ]
        verbose_name = "Post Image"


    

class Post(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name=_("User"))
    title = models.CharField(max_length=250, verbose_name=_("Title"))

    keywords = models.TextField(null=True, blank=True, verbose_name=_("Meta keywords"))
    description = models.TextField(null=True, blank=True, verbose_name=_("Meta description"))

    excerpt = models.TextField(max_length=250, null=True, blank=True, verbose_name=_("Excerpt"))
    content = models.TextField(verbose_name=_("Content"))
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=_("Tags"), related_name="posts")
    post_image = models.ForeignKey(PostImage, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_("Post image"), related_name="the_posts")
    featured = models.BooleanField(default=settings.POST_FEATURED, verbose_name=_("Featured"))
    allow_comments = models.BooleanField(default=settings.POST_ALLOW_COMMENTS, verbose_name=_("Allow comments"))
    show_comments = models.BooleanField(default=settings.POST_SHOW_COMMENTS, verbose_name=_("Show comments"))
    published = models.BooleanField(default=settings.POST_PUBLISHED, verbose_name=_("Published"))



    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    def __str__(self):
        return f"#{self.id} - {self.title}"
    

    def get_excerpt(self, char_count=100):
        if self.excerpt:
            return self.excerpt[:char_count] + " ..."
        return self.content[:char_count] + " ..."
    

    @admin.display(description=_("Image preview"))
    def get_image_tag(self):
        if self.post_image:
            return self.post_image.get_image_tag()
        return None
    
    @admin.display(description=_("Image preview link"))
    def get_image_tag_link(self):
        if self.post_image:
            return self.post_image.get_image_tag_link()
        return None
    
    @admin.display(description=_("Image URL"))
    def get_image_url(self):
        if self.post_image:
            return self.post_image.get_image_url()
        return None
    
    @admin.display(description=_("Image Link"))
    def get_image_link(self):
        if self.post_image:
            return self.post_image.get_image_link()
        return None
    
    class Meta:
        ordering = [
            "-created_at"
        ]
        verbose_name = _("Post")




class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=_("Post"), related_name="comments")
    email = models.EmailField(verbose_name=_("Email"))
    text = models.TextField(verbose_name=_("Text"))
    published = models.BooleanField(default=True, verbose_name=_("Published"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    def __str__(self):
        return f"{ſelf.email} - {self.text_excerpt} - [{self.post}]" 

    @property
    def text_excerpt(self):
        return self.text[:20] + " ..."
    
    @property
    def email_excerpt(self): 
        return self.email[:20] + " ..."

    class Meta:
        ordering = [
            "-created_at"
        ]
        verbose_name = _("Comment")


    


