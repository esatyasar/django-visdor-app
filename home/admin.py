from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone_number",
        "email",
        "message",
        "created_date",
    )

    list_filter = ("name",)
    search_fields = ("name_startswith",)
    
    
admin.site.register(Contact,ContactAdmin)

# Register your models here.
