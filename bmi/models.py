from django.db import models
from django.urls import reverse_lazy
from django.utils.timezone import now
# Create your models here.
#BMI_

class BMI(models.Model):
    name = models.CharField(max_length=20 , unique = True)
    height = models.FloatField()
    weight = models.FloatField()
    bmi = models.FloatField(blank=True , null=True )

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.bmi = self.weight/((self.height/100)**2)

        super(BMI, self).save(force_insert, force_update, using, update_fields)

   # 이름바꾸기
    def __str__(self):
        return self.name+"의 BMI"

    def get_absolute_url(self):
        return reverse_lazy('bmi_detail', args= [self.id])
