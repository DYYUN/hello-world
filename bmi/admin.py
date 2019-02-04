from django.contrib import admin
from .models import *


class BMIAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'height', 'weight', 'bmi' ]

admin.site.register(BMI, BMIAdmin)
# Register your models here.

#내가 작성한 모데을 관리자 페이지에서 관리할 수 있도록 추가
#관리자 페이지의 목록이나 기능을 커스터마이징하는 옵션을 추가

