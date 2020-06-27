from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
import random
from products.models import Product


def random_string():
    return str(random.randint(1, 10000))

class Salary(models.Model):
    name                    = models.CharField(_("إسم الفتورة"),max_length=150)
    typeofproducts   = models.ForeignKey('products.Product', verbose_name=_("typeofproducts"), on_delete=models.CASCADE)
    code                      = models.IntegerField(_("كود المنتج"), default=random_string)
    description          = models.TextField(_("وصف المنتج"))
    address                = models.CharField(_("العنوان"),max_length=150)
    create_at             = models.DateTimeField(_("تاريخ الإضافة"), default = timezone.now) 
    update_by           = models.DateTimeField(_("تم التحديث :"),auto_now_add=True, blank=True, null=True)
    price                     = models.FloatField(_("سعر المنتج"))
    count                    = models.FloatField(_("الكمية"))
    profit                    = models.FloatField(_("سعر الفتورة "),blank=True, null=True)

    class Meta:
        verbose_name = _("Salary")
        verbose_name_plural = _("Salarys")

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if self.profit or not self.profit:
           self.profit = self.count * self.price
        super(Salary, self).save(*args, **kwargs)


class Purchasing(models.Model):
    name                    = models.CharField(_("إسم الفتورة"),max_length=150)
    code                      = models.IntegerField(_("كود المنتج"), default=random_string)
    description          = models.TextField(_("وصف الفتورة"))
    address                    = models.CharField(_("العنوان"),max_length=150)
    create_at             = models.DateTimeField(_("تاريخ الإضافة"), default = timezone.now) 
    update_by            = models.DateTimeField(_("تم التحديث :"),auto_now_add=True, blank=True, null=True)
    price                     = models.FloatField(_("سعر المنتج"))
    count                    = models.FloatField(_("الكمية"))
    profit                    = models.FloatField(_("سعر الفتورة"),blank=True, null=True)

    class Meta:
        verbose_name = _("Purchasing")
        verbose_name_plural = _("Purchasings")

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if self.profit or not self.profit:
           self.profit = self.count * self.price
        super(Purchasing, self).save(*args, **kwargs)

class Customer(models.Model):
    name                    = models.CharField(_("إسم العميل"),max_length=150)
    code                      = models.IntegerField(_("كود العميل"), default=random_string)
    phone1                    = models.IntegerField(_("رقم العميل "))
    phone2                    = models.IntegerField(_("إضافة رقم ثانى"))
    phone3                    = models.IntegerField(_("إضافة رقم ثالث"))
    description          = models.TextField(_("وصف العميل"))
    address                 = models.CharField(_("العنوان"),max_length=150)
    create_at             = models.DateTimeField(_("تاريخ الإضافة"), default = timezone.now) 
    update_by            = models.DateTimeField(_("تم التحديث :"),auto_now_add=True, blank=True, null=True)
    old_profit             = models.FloatField(_(" البضاعة المسحوبة حتى الأن"),blank=True, null=True)
    profit                    = models.FloatField(_(" البضاعة الجديدة"),blank=True, null=True)

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.old_profit = self.old_profit + self.profit 
        super(Customer, self).save(*args, **kwargs)