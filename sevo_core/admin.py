from django.contrib import admin
from django.contrib.auth import get_user_model

from sevo_core import models



class BaseUserMixinAdmin(admin.ModelAdmin):
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
