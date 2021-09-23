from django.contrib import admin
from quoteapp.models import Author,Quotes

class AuthorAdmin(admin.ModelAdmin):
        search_fields = ['name']
        ordering = ['name']

class QuotesAdmin(admin.ModelAdmin):
        list_display = ('id', 'quote_text', 'author')
        list_display_links = ('quote_text',)
        search_fields = ['quote_text']
        list_filter = ['author']
        ordering = ['id']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Quotes, QuotesAdmin)