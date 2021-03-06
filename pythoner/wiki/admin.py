#encoding:utf-8
"""
pythoner.net
Copyright (C) 2013  PYTHONER.NET

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from django.contrib import admin
from wiki.models import *

class EntryAdmin(admin.ModelAdmin):
    list_display = ('title','category','sub_time','click_time','public')
    list_display_links = ('title','category')

class TagAdmin(admin.ModelAdmin):
    list_display = ('name','remark')
    list_display_links = ('name','remark')

admin.site.register(Entry,EntryAdmin)
admin.site.register(Category)
admin.site.register(Tag,TagAdmin)
