from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from app.models import PatientInfo
from app.models import SampleType
from app.models import CancerType
from app.models import SurgeryMethod
from app.models import Medication
from app.models import Box
from app.models import BoxPosition
from app.models import SampleRecord


@admin.register(PatientInfo)
class PatientInfoAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'no_of_patient',
        'name',
        'gender',
        'birthday',
        'created_at',
        'updated_at',
        'user',
        'is_disable',
    )


@admin.register(SampleType)
class SampleTypeAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'name',
        'created_at',
        'updated_at',
        'user',
        'is_disable',
    )


@admin.register(CancerType)
class CancerTypeAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'name',
        'created_at',
        'updated_at',
        'user',
        'is_disable',
    )


@admin.register(SurgeryMethod)
class SurgeryMethodAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'name',
        'created_at',
        'updated_at',
        'user',
        'is_disable',
    )


@admin.register(Medication)
class MedicationAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'name',
        'created_at',
        'updated_at',
        'user',
        'is_disable',
    )


@admin.register(Box)
class BoxAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'no_of_box',
        'created_at',
        'updated_at',
        'user',
        'is_disable',
    )


@admin.register(BoxPosition)
class BoxPositionAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'box',
        'position',
        'is_used',
        'created_at',
        'updated_at',
        'user',
        'is_disable',
    )


@admin.register(SampleRecord)
class SampleRecordAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'patient',
        'date_of_received_sample',
        'sample_type',
        'date_of_surgery',
        'cancer_type',
        'surgery_method',
        'medication',
        'sample_position',
        'afp',
        'lung_shung',
        'created_at',
        'updated_at',
        'user',
        'is_disable',
    )




