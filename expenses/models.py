from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

class Workers(models.Model):
    TYPE_OF_PERSON = {
        ('صنايعي' , "صنايعي" ),
        ('عامل' , "عامل" ),
        ('إداري' , "إدارى" ),
        ('محاسب' , "محاسب" ),
        ('سواق' , "سواق" ),
    }
    name                               = models.CharField(_("إسم العامل"),max_length=150)
    type_of_person              = models.CharField(_("نوع العامل"), max_length=50 ,choices=TYPE_OF_PERSON, default='عامل' )
    description                     = models.TextField(_("وصف العامل"))
    create_at                        = models.DateTimeField(_("تاريخ الإضافة"), default = timezone.now) 
    update_by                       = models.DateTimeField(_("تم التحديث :"),auto_now_add=True, blank=True, null=True)
    price                                = models.FloatField(_("راتب العامل "))

    class Meta:
        verbose_name = _("Workers")
        verbose_name_plural = _("Workerss")

    def __str__(self):
        return str(self.name)

    # def save(self, *args, **kwargs):
    #     self.remaining_amount = self.price - self.amount_received
    #     super(Workers, self).save(*args, **kwargs)




class Amount_Received(models.Model):
    workers                          = models.ForeignKey("Workers", verbose_name=_("العامل"), on_delete=models.CASCADE)
    amount_received           = models.FloatField(_("قيمة السلفة"))
    remaining_amount        = models.FloatField(_("صافي المرتب "), blank=True, null=True)
    description                     = models.TextField(_("سبب السلفة"))
    create_at                        = models.DateTimeField(_("تاريخ الإضافة"), default = timezone.now) 
    update_by                       = models.DateTimeField(_("تم التحديث :"),auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name             = _("Rmount_Received")
        verbose_name_plural = _("Rmount_Receiveds")

    def __str__(self):
        return str(self.workers)

    def save(self, *args, **kwargs):
        self.remaining_amount = self.workers.price - self.amount_received
        super(Amount_Received, self).save(*args, **kwargs)





class Servicing(models.Model):
    name                              = models.CharField(_("عنوان الصيانة"),max_length=150)
    description                    = models.TextField(_("وصف الصيانة"))
    create_at                       = models.DateTimeField(_("تاريخ الإضافة"), default = timezone.now) 
    update_by                      = models.DateTimeField(_("تم التحديث :"),auto_now_add=True, blank=True, null=True)
    cost                                = models.FloatField(_("تكلفة الصيانه"))

    class Meta:
        verbose_name = _("Servicing")
        verbose_name_plural = _("Servicings")

    def __str__(self):
        return str(self.name)

