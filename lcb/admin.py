from django.contrib import admin

from lcb.models import Board, Lane, Card


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'owner', 'phase', 'vote_limit', 'think_time_limit', 'discuss_time_limit']
    ordering = ['-created']


@admin.register(Lane)
class LaneAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'board', 'position']
    ordering = ['board', 'position']


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'board', 'lane', 'owner', 'position']
    ordering = ['board', 'position']
