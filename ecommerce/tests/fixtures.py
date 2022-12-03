import pytest

@pytest.fixture
def create_admin_user(django_user_model): #django_user_model allows us to select user model, a tool from pytest.django automatically selects user model
    """
    Return admin user
    """
    return django_user_model.objects.create_superuser("admin", "a@a.com", "password") #so it creates a super user in this default user table