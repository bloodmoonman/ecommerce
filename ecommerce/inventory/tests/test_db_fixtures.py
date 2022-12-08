import pytest

from ecommerce.inventory import models

# need models to test database


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, slug, is_active",  # these are the table fields in the category
    [
        (1, "fashion", "fashion", 1), # "id, name, slug, is_active"
        (18, "trainers", "trainers", 1),
        (35, "baseball", "baseball", 1)
    ],  # need some data to test
)
def test_inventory_category_dbfixture( #this tests the db fixture
    db, db_fixture_setup, id, name, slug, is_active):
    result = models.Category.objects.get(id=id)  # id gets 1, 18, 38 from parameterization

    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active



@pytest.mark.parametrize("slug, is_active", [("fashion", 1), ("trainers", 1), ("baseball", 1)])
def test_inventory_db_category_insert_data(db, category_factory, slug, is_active): #this tests if we can insert a data to db
    #category_factory will allow us to build data for our new model
    result = category_factory.create(slug=slug, is_active=is_active) #passing the data to factory
    print(result.name)
    assert result.slug == slug
    assert result.is_active == is_active


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [

    ],
)