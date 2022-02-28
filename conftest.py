from os import lseek
import pytest
from django.contrib.auth.models import User
from pytest_factoryboy import register
from tests.factories import UserFactory

register(UserFactory) # access to this factory available by  "user_factory"



@pytest.fixture
def new_user1(db, user_factory):
    user = user_factory.create()
    return user 






# @pytest.fixture
# def user_1(db):
#     user = User.objects.create_user('test-user')
#     return user

# @pytest.fixture
# def new_user_factory(db):
#     def create_app_user(
#         username: str,
#         password: str,
#         first_name: str = 'firstname',
#         last_name: str = 'lastname',
#         email: str = 't@t.com',
#         is_staff: str = False,
#         is_superuser: str = False,
#         is_active: str = True):
    
#         user = User.objects.create_user(
#             username=username,
#             password=password,
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#             is_staff=is_staff,
#             is_superuser=is_superuser,
#             is_active=is_active
#         )
#         return user
#     return create_app_user

# @pytest.fixture
# def new_user(db, new_user_factory):
#     return new_user_factory("test_user","password", "myname")

# @pytest.fixture
# def new_user1(db, new_user_factory):
#     return new_user_factory("test_user1","password", "myname1", is_staff=True)








