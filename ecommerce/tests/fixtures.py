import pytest
from django.contrib.auth.models import User
from django.core.management import call_command

@pytest.fixture
def create_admin_user(django_user_model): #django_user_model allows us to select user model, a tool from pytest.django automatically selects user model
    """
    Return admin user
    """
    return django_user_model.objects.create_superuser("admin", "a@a.com", "password") #so it creates a super user in this default user table



@pytest.fixture(scope="session")
def db_fixture_setup(django_db_setup, django_db_blocker):
    """
    Load DB data fixtures
    """

    with django_db_blocker.unblock():
        return call_command("loaddata", "db_admin_fixture.json")