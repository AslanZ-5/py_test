import pytest 



@pytest.mark.django_db
def test_set_check_password(user_1): 
    print('ok?')
    user_1.set_password("new-password")
    assert user_1.check_password("new-password") is True

def test_set_check_name(user_1):
    print('ok?')
    assert user_1.username == 'test-user'
   

def test_new_user(new_user):
    print('test_new_user1----', new_user.username)
    assert new_user.username == 'test_user'


def test_new_user_firstname(new_user):
    print('test_new_user2----', new_user.first_name)
    assert new_user.first_name == 'myname'