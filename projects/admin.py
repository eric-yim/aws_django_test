from django.contrib import admin

from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    #fields = ['url_str','pub_date', 'description']
    fieldsets = [
        ('Back',               {'fields': ['url_str','pub_date']}),
        ('Front',               {'fields': ['description','image_url','snippet','body_html']})
    ]

admin.site.register(Project,ProjectAdmin)

#admin.site.register(Project)
