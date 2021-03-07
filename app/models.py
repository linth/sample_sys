from django.db import models
from django.contrib.auth.models import User

"""
注意事項:
1. 建立model時候，應該注意哪些內容格式要如何?
    - https://www.liujiangblog.com/course/django/100
    - https://medium.com/my-back-end-life/django-%E6%A8%A1%E5%9E%8B%E7%B9%BC%E6%89%BF-85358f81e325
2. 
"""


class Base(models.Model):
    """ the basic model information. """
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_disable = models.BooleanField(default=False)

    class Meta:
        abstract = True


class PatientInfo(Base):
    """ the basic information for patient. """
    SEX = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    no_of_patient = models.CharField(max_length=300)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=SEX)
    birthday = models.DateField()

    class Meta:
        app_label = 'app'
        db_table = 'patient_info'
        managed = True
        ordering = ['no_of_patient']

    def __str__(self):
        return self.no_of_patient


class SampleType(Base):
    """ the category of sample. """
    name = models.CharField(max_length=300, unique=True)

    class Meta:
        app_label = 'app'
        db_table = 'sample_type'
        managed = True
        ordering = ['name']

    def __str__(self):
        return self.name


class CancerType(Base):
    """ the category of cancer. """
    name = models.CharField(max_length=300, unique=True)

    class Meta:
        app_label = 'app'
        db_table = 'cancer_type'
        managed = True
        ordering = ['name']

    def __str__(self):
        return self.name


class SurgeryMethod(Base):
    """ the category of surgery. """
    name = models.CharField(max_length=300, unique=True)

    class Meta:
        app_label = 'app'
        db_table = 'surgery_method'
        managed = True
        ordering = ['name']

    def __str__(self):
        return self.name


class Medication(Base):
    """ the category of medication. """
    name = models.CharField(max_length=300, unique=True)

    class Meta:
        app_label = 'app'
        db_table = 'medication'
        managed = True
        ordering = ['name']

    def __str__(self):
        return self.name


class Box(Base):
    """ the information of box. """
    no_of_box = models.IntegerField(unique=True)

    class Meta:
        app_label = 'app'
        db_table = 'box'
        managed = True
        ordering = ['no_of_box']

    def __str__(self):
        return str(self.no_of_box)


class BoxPosition(Base):
    """ the position of box. """
    box = models.ForeignKey(Box, on_delete=models.CASCADE, blank=True, null=True)
    position = models.IntegerField(blank=False, null=False, unique=True)
    is_used = models.BooleanField(default=False)

    class Meta:
        app_label = 'app'
        db_table = 'box_position'
        managed = True
        ordering = ['box__no_of_box', 'position']

    def __str__(self):
        return str(self.box) + '-' + str(self.position)


class SampleRecord(Base):
    """ the record for patient. """
    patient = models.ForeignKey(PatientInfo, on_delete=models.CASCADE)
    date_of_received_sample = models.DateField() # 檢體收檢日期
    sample_type = models.ForeignKey(SampleType, on_delete=models.CASCADE) # 檢體類型
    date_of_surgery = models.DateField() # 手術日期
    cancer_type = models.ForeignKey(CancerType, on_delete=models.CASCADE) # 癌別
    surgery_method = models.ForeignKey(SurgeryMethod, on_delete=models.CASCADE) # 手術方式
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE) # 用藥
    sample_position = models.ForeignKey(BoxPosition, on_delete=models.CASCADE, blank=True, null=True)

    # 一般生化
    afp = models.FloatField() # AFP
    lung_shung = models.FloatField() # Lung Shung

    class Meta:
        app_label = 'app'
        db_table = 'sample_record'
        managed = True
        ordering = ['-updated_at', '-created_at', 'patient']

    def __str__(self):
        return str(self.id)


