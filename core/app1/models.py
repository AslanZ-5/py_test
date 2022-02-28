from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Category(models.Model):
    """
     Category Table implemented with WPTT
    """
    name = models.CharField(
        verbose_name= _("Category name"),
        help_text= _("Required and unique"),
        max_length=255,
        unique=True
    )
    slug = models.SlugField(verbose_name= _("Category safe URL"), max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural= _("Categories")
    
    
    def __str__(self):
        return self.name



class Product(models.Model):
    """
    The Product table contining all product items.
    """
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    title = models.CharField(
        verbose_name= _("title"),
        help_text= _("Required"),
        max_length=255,
    )
    description = models.TextField(verbose_name= _("descritpion"), help_text= _("Not Required"), blank=True)
    slug = models.SlugField(max_length=255)
    regular_price = models.DecimalField(
        verbose_name= _("Regular price"),
        help_text= _("Maximum 999.999"),
        max_digits=5,
        error_messages= {
            "name":{
                "max_length": _('The price must be between 0 and 999.99')
            },
        },
        decimal_places=2,
    )
    discount_price = models.DecimalField(
        verbose_name= _("Discount price"),
        help_text= _("Maximum 999.99"),
        max_digits=5,
        error_messages= {
            "name":{
                "max_length": _('The price must be between 0 and 999.99')
            },
        },
        decimal_places=2,
    )
    is_active = models.BooleanField(
        verbose_name= _("Product visibility"),
        help_text= _("Change product visibihity"),
        default=True,
    )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)
    users_wishlist = models.ManyToManyField(User, related_name="user_wishlist",blank=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    
    def __str__(self):
        return self.title