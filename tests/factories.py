from operator import imod
import factory
from faker import Faker
from django.contrib.auth.models import User
from core.app1.models import Category, Product
fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    
    username = fake.name()
    is_staff = True


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    
    name = 'django'
    slug = 'django'


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
    category = factory.SubFactory(CategoryFactory)
    title = "product_title"
    description = fake.text()
    slug = "product_slug"
    regular_price = "12.91"
    discount_price = "22.72"
    