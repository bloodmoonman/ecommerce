import factory
import pytest
from faker import Faker #will allow us to generate data automatically
from pytest_factoryboy import register
from ecommerce.inventory import models

fake = Faker()

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    name = fake.lexify(text="cat_name_??????") #lexify allows us to create random elements. ? does make those random elements for us. Everytime we create a factory because of lexify and ?? the name will be different
                                               #named it cat because this way we can recognize that it is the Category field, we can understand where this data is coming from
    slug = fake.lexify(text="cat_slug_??????") #everytime we utilize this factory it is going to generate a new entry in the database. thats the point of this factory

register(CategoryFactory) #registered and now it becomes available
