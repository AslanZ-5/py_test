import pytest
from core.app1.models import Product

def test_new_user(new_user1):
    print('???????????????',new_user1.username)
    assert True

def test_product(db,product_factory):
    product = product_factory.create()
    print('^^^^^^^^^^',product.description)
    assert True

@pytest.mark.parametrize(
    "category, title, description, slug, regular_price, discount_price, validity",
    [
        ("NewTitle", 1, "NewDescription", 'slug', '4.55', '2.33', True),
        ("NewTitle", 1, "NewDescription", 'slug', '4.55', '', False)
    ],
)
@pytest.mark.django_db
def test_product_instance(
    product_factory, category, title, description, slug, regular_price, discount_price, validity):
    test = product_factory(
        title = title,
        category_id = category,
        description = description,
        slug = slug,
        regular_price = regular_price,
        discount_price = discount_price,
    )
    item = Product.objects.all().count()
    assert item == validity
