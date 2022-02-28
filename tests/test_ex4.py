def test_new_user(new_user1):
    print('???????????????',new_user1.username)
    assert True

def test_product(product_factory):
    product = product_factory.build()
    print('^^^^^^^^^^',product.description)