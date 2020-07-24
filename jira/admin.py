from django.contrib import admin

# Register your models here.

from jira.models.m_users import Account

admin.site.register(Account)