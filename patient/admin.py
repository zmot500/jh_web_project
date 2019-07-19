from django.contrib import admin
from patient.models import Patient, Check


# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display=("idx", "Pt_name", "Pt_bdate", "Pt_man")
    
class CheckAdmin(admin.ModelAdmin):
    list_display=("idx", "in_date", "in_db", "in_wt", "in_bp_l", "in_bp_h" )
    
admin.site.register(Patient, PatientAdmin)
admin.site.register(Check, CheckAdmin)
# Register your models here.
