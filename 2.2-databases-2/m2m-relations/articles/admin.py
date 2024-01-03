from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from articles.models import Article, Scope, Tag



class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_list = []
        for form in self.forms:


            bool = form.cleaned_data.get('is_main')
            is_main_list.append(bool)
            if is_main_list.count(True) > 1:
                raise ValidationError('Основной раздел может быть только один')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    fields = ['tag', 'is_main']
    formset = ScopeInlineFormset
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'published_at', 'image',)
    list_filter = ('title','published_at',)
    inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ('is_main', 'article', 'tag',)
    list_filter = ('is_main', 'article', 'tag',)