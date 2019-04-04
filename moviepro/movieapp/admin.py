from django.contrib import admin
from.models import Telugu,English,Hindhi
class AdminTelugu(admin.ModelAdmin):
    list_display = ['director_name','hero_name','heroin_name','product_name','released_date']
class AdminEnglish(admin.ModelAdmin):
    list_display = ['director_name','hero_name','heroin_name','product_name','released_date']
class AdminHindhi(admin.ModelAdmin):
    list_display = ['director_name','hero_name','heroin_name','product_name','released_date']
admin.site.register(Telugu,AdminTelugu)
admin.site.register(English,AdminEnglish)
admin.site.register(Hindhi,AdminHindhi)