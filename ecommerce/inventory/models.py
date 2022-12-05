from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField

class Category(MPTTModel):
    name = models.CharField(max_length=100, null=False, unique=False, blank=False, verbose_name=_("category name"), help_text=_("format: required, max-100")) 
                                                                                                        # _ gets those translated because gettext_lazy as _  - help text is additional info for user means this field is required and max_length is 100
    slug = models.SlugField()                                                                                                                               
    
    