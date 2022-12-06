from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField

class Category(MPTTModel):
    name = models.CharField(max_length=100, null=False, unique=False, blank=False, verbose_name=_("category name"), help_text=_("format: required, max-100")) 
                                                                                                        # _ gets those translated because gettext_lazy as _  - help text is additional info for user means this field is required and max_length is 100
    slug = models.SlugField(max_length=150, null=False, unique=False, verbose_name=_("category safe URL"), help_text=_("format: required, letters, numbers, underscore or hypens"))
    is_active = models.BooleanField(default=True)                                                                                                                               

    parent = TreeForeignKey("self", on_delete=models.PROTECT, related_name="children", null=True, blank=True, unique=False, verbose_name=_("parent of category"), help_text=_("format: not required")) #this is part of mptt model setup, this field will allow us to connect to the parent field

    class MPTT:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("product category") #that is going to be the name of the table
        verbose_name_plural = _("product categories") #if you don't define this plural everywhere in your system is going to say category  
    
    def __str__(self):
        return self.name
     