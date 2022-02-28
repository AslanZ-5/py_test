import pytest 
from django.contrib.auth.models import User


# @pytest.mark.django_db
# def test_set_check_password(user_1): 
#     print('ok?')
#     user_1.set_password("new-password")
#     assert user_1.check_password("new-password") is True

# def test_set_check_name(user_1):
#     print('ok?')
#     assert user_1.username == 'test-user'
   
@pytest.mark.django_db
def test_new_user(user_factory):
    # user = user_factory.build() # creating an object not saving into data base
    user = user_factory.create() # creating an object and saving into data base
    count = User.objects.all().count()
    print(count)
    print('test_new_user1----', user.username)
    assert True


# def test_new_user_firstname(new_user):
#     print('test_new_user2----', new_user.first_name)
#     assert new_user.first_name == 'myname'

# def test_new_user_firstname(new_user1):
#     print('test_new_user3----', new_user1.is_staff)
#     assert new_user1.is_staff == True