from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
import random
from django.template.defaultfilters import floatformat

def random_string():
    return str(random.randint(10000, 99999))

class ProductMix(models.Model):

    TYPE_OF_ProductMix={
        ('بولى اثلين' , 'بولى اثلين'),
        ('الصبغة ' , 'الصبغة '),
        ('الأوميالين' , 'الأوميالين'),
        ('ريسايكل' , 'ريسايكل'),
        ('تخريز' , 'تخريز'),

    }
    name               = models.CharField(_("إسم الخلطة "), max_length=150)
    code                 = models.IntegerField(_("كود الخلطة"), default=random_string)
    image              = models.ImageField(_("صورة الخلطة"), upload_to='ProductMix_Image',blank=True, null=True)
    
    type1               = models.CharField(_("إسم الخامة الأولى"), choices=TYPE_OF_ProductMix ,max_length=50)
    type1_count   = models.FloatField(_("نسبة الخامة الأولى"), blank=True, null=True)
    type1_price     = models.FloatField(_("سعر الخامة الأولى"), blank=True, null=True)
    price1     = models.FloatField(_("سعر الخامة فى الخلطة سيتم حسابة تلقائي"), blank=True, null=True)
    
    type2              = models.CharField(_("إسم الخامة الثانية"), choices=TYPE_OF_ProductMix ,max_length=50)
    type2_count   = models.FloatField(_("نسبة الخامة الثانية"), blank=True, null=True)
    type2_price     = models.FloatField(_("سعر الخامة الثانية"), blank=True, null=True)
    price2     = models.FloatField(_("سعر الخامة فى الخلطة سيتم حسابة تلقائي"), blank=True, null=True)

    type3               = models.CharField(_("إسم الخامة الثالثة"), choices=TYPE_OF_ProductMix ,max_length=50)
    type3_count   = models.FloatField(_("نسبة الخامة الثالثة"), blank=True, null=True)
    type3_price     = models.FloatField(_("سعر الخامة الثالثة"), blank=True, null=True)
    price3     = models.FloatField(_("سعر الخامة فى الخلطة سيتم حسابة تلقائي"), blank=True, null=True)

    type4               = models.CharField(_("إسم الخامة الرابعة"), choices=TYPE_OF_ProductMix ,max_length=50)
    type4_count   = models.FloatField(_("نسبة الخامة الرابعة"), blank=True, null=True)
    type4_price     = models.FloatField(_("سعر الخامة الرابعة"), blank=True, null=True)
    price4     = models.FloatField(_("سعر الخامة فى الخلطة سيتم حسابة تلقائي"), blank=True, null=True)

    type5               = models.CharField(_("إسم الخامة الخامسة"), choices=TYPE_OF_ProductMix ,max_length=50)
    type5_count   = models.FloatField(_("نسبة الخامة الخامسة"), blank=True, null=True)
    type5_price     = models.FloatField(_("سعر الخامة الخامسة"), blank=True, null=True)
    price5     = models.FloatField(_("سعر الخامة فى الخلطة سيتم حسابة تلقائي"), blank=True, null=True)

    description     = models.CharField(_("الوصفة بشكل عام"),max_length=300,blank=True, null=True)
    create_at        = models.DateTimeField(_("تاريخ الإضافة"), default = timezone.now) 
    update_by       = models.DateTimeField(_("تم التحديث :"),auto_now_add=True, blank=True, null=True)
    price                   = models.FloatField(_("سعر الخلطة"), blank=True, null=True)

    class Meta:
        verbose_name = _("Product_Mix")
        verbose_name_plural = _("Product_Mixs")

    def __str__(self):
        return '%s %s' %(self.name , self.price)


    def save(self, *args , **kwargs):
        self.price1 = self.type1_price * self.type1_count
        self.price2 = self.type2_price * self.type2_count
        self.price3 = self.type3_price * self.type3_count
        self.price4 = self.type4_price * self.type4_count
        self.price5 = self.type5_price * self.type5_count
        
        self.price = self.price1 + self.price2 + self.price3 + self.price4 + self.price5
        super(ProductMix , self).save(*args , **kwargs)


class Roll(models.Model):
    productmix     = models.ForeignKey( ProductMix, verbose_name=_(" إسم الخلطة "), on_delete=models.CASCADE)
    name               = models.CharField(_("إسم اللفة "), max_length=150)
    size                    = models.FloatField(_("وزن اللفة"))
    code                 = models.IntegerField(_("كود اللفة"), default=random_string)
    image              = models.ImageField(_("صورة اللفة"), upload_to='Roll_Image',blank=True, null=True)
    description     = models.TextField(_("وصف اللفة"))
    create_at        = models.DateTimeField(_("تاريخ الإضافة"), default = timezone.now) 
    update_by       = models.DateTimeField(_("تم التحديث :"),auto_now_add=True, blank=True, null=True)
    cost                 = models.ForeignKey( ProductMix, verbose_name=_("تكلفة الكيلو"),related_name='ProductMixcost', on_delete=models.CASCADE)
    price                = models.FloatField(_("سعر الكيلو فى اللفة"))
    roll_price          = models.FloatField(_("السعر الكلى للفة"),blank=True, null=True)
    profit               = models.FloatField(_("هامش الربح"),blank=True, null=True)
    
    class Meta:
        verbose_name = _("Roll")
        verbose_name_plural = _("Rolls")

    def __str__(self):
        return '%s %s' %(self.productmix ,self.name)

    def save(self, *args , **kwargs):
        self.roll_price = self.size * self.price
        self.profit = self.size * self.cost.price - self.roll_price
        super(Roll , self).save(*args , **kwargs)


    def Update_Roll(self): #Updating the value of another model in Django Models
        roll_productmix = self.productmix
        roll_productmix.price = self.cost.price
        roll_productmix.save()



class Product(models.Model):
    roll                    = models.ForeignKey(Roll, verbose_name=_("إسم الخلطة واللفة"), on_delete=models.CASCADE)
    name               = models.CharField(_("إسم المنتج "), max_length=50)
    size                    = models.FloatField(_("حجم الكيس"))
    code                 = models.IntegerField(_("كود المنتج"), default=random_string)
    image              = models.ImageField(_("صورة المنتج"), upload_to='Product_Image',blank=True, null=True)
    description     = models.TextField(_("وصف المنتج"))
    create_at        = models.DateTimeField(_("تاريخ الإضافة"), default = timezone.now) 
    update_by          = models.DateTimeField(_("تم التحديث :"),auto_now_add=True, blank=True, null=True)
    cost                 = models.ForeignKey(Roll, verbose_name=_("سعر الخلطة"), related_name='costroll' , on_delete=models.CASCADE)
    price                = models.FloatField(_("سعر المنتج"))
    profit               = models.FloatField(_("هامش الربح"),blank=True, null=True)
    
    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
           self.profit = self.cost.price - self.price
           super(Product, self).save(*args, **kwargs)

    def Update_Roll(self): #Updating the value of another model in Django Models
        product_roll = self.roll
        product_roll.cost = self.cost.price
        product_roll.save()