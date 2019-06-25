# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

#Import models
from mi_tienda.models import ClaseA
from mi_tienda.models import Berlinas

# Register your models here.
admin.site.register(ClaseA)
admin.site.register(Berlinas)
