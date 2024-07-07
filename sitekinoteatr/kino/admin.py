from django.contrib import admin
from .models import Genre, Director, Actor, Movie, Session, Ticket
from django.core.management import call_command

class GenreAdmin(admin.ModelAdmin):
    search_fields = ['name']

class DirectorAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo']
    search_fields = ['name']

class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo']
    search_fields = ['name']

class ActorInline(admin.TabularInline):
    model = Movie.actor.through
    extra = 1

class SessionAdmin(admin.ModelAdmin):
    list_display = ['movie', 'time', 'hall']
    search_fields = ['movie__title']
    list_filter = ['time', 'hall']

class TicketAdmin(admin.ModelAdmin):
    list_display = ['user', 'session', 'seat']
    search_fields = ['user__username', 'session__movie__title']
    list_filter = ['session__time']

def fill_fake_data(modeladmin, request, queryset):
    call_command('fill_fake_data')

fill_fake_data.short_description = 'Заполнить фейковыми данными'

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'director']
    search_fields = ['title', 'description']
    list_filter = ['genre', 'director']
    actions = [fill_fake_data]

admin.site.register(Genre, GenreAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Ticket, TicketAdmin)
