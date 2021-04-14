from django.contrib import admin

from lcb.models import Board, BoardMember, Lane, Card


class BoardMemberInline(admin.TabularInline):
    model = BoardMember
    extra = 0
    fields = ['user', 'joined']
    readonly_fields = ['joined']


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created', 'owner', 'phase', 'vote_limit', 'think_time_limit', 'discuss_time_limit']
    ordering = ['-created']
    inlines = [BoardMemberInline]


@admin.register(Lane)
class LaneAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'board', 'type', 'position']
    ordering = ['board', '-type', 'position']


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'board', 'lane', 'owner', 'position']
    ordering = ['board', 'lane', 'position']
