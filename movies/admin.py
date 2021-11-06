from django.contrib import admin
from .models import *

class ViewReview(admin.StackedInline):
        model=Review
        extra=1


class CustomMovieModel(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name','rate','likes','custom_column')
    readonly_fields=('custom_column',)
    fieldsets = (
        ('Main', {'fields': ('name','description',) }),
        ('Numerical data', {'fields': ('rate', 'likes','custom_column',)}),
        ('Media', {'fields': ('poster',)}),
        ('Date', {'fields': ('production_date',)}),
        ('Info', {'fields': ('actors','categories',)}),
        ('unique', {'fields': ('code',)}),
    )
    inlines = [ViewReview]
    def custom_column(self,obj):
        #just for trial, doesn't have any meaning
        if obj.rate and obj.likes:
            return obj.rate + obj.likes
        return obj.likes

admin.site.register(Movie,CustomMovieModel)
admin.site.register(Actor)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Code)





