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


@pytest.mark.dbfixture #
@pytest.mark.parametrize(
    "id, web_id, name, slug, description, is_active, created_at, updated_at,",
    [(
        1,
        "45425810",
        "widstar running sneakers",
        "widstar-running-sneakers",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin porta, eros vel sollicitudin lacinia, quam metus gravida elit, a elementum nisl neque sit amet orci. Nulla id lorem ac nunc cursus consequat vitae ut orci. In a velit eu justo eleifend tincidunt vel eu turpis. Praesent eu orci egestas, lobortis magna egestas, tincidunt augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean vitae lectus eget tortor laoreet efficitur vel et leo. Maecenas volutpat eget ante id tempor. Etiam posuere ex urna, at aliquet risus tempor eu. Aenean a odio odio. Nunc consectetur lorem ante, interdum ultrices elit consectetur sit amet. Vestibulum rutrum interdum nulla. Cras vel mi a enim eleifend blandit. Curabitur ex dui, rutrum et odio sit amet, auctor euismod massa.",
        1,
        "2021-09-04 22:14:18",
        "2021-09-04 22:14:18",
    ),
    (
        8616,
        "45434425",
        "impact puse dance shoe",
        "impact-puse-dance-shoe",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin porta, eros vel sollicitudin lacinia, quam metus gravida elit, a elementum nisl neque sit amet orci. Nulla id lorem ac nunc cursus consequat vitae ut orci. In a velit eu justo eleifend tincidunt vel eu turpis. Praesent eu orci egestas, lobortis magna egestas, tincidunt augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean vitae lectus eget tortor laoreet efficitur vel et leo. Maecenas volutpat eget ante id tempor. Etiam posuere ex urna, at aliquet risus tempor eu. Aenean a odio odio. Nunc consectetur lorem ante, interdum ultrices elit consectetur sit amet. Vestibulum rutrum interdum nulla. Cras vel mi a enim eleifend blandit. Curabitur ex dui, rutrum et odio sit amet, auctor euismod massa.",
        1,
        "2021-09-04 22:14:18",
        "2021-09-04 22:14:18",
        ),
    ],)
def test_inventory_db_product_dbfixture(db, db_fixture_setup, id, web_id, name, slug, description, is_active, created_at, updated_at):
    result = models.Product.objects.get(id=id)
    result_created_at = result.created_at.strftime("%Y-%m-%d %H:%M:%S") #formatting the data from the database so we can match up with the data above(parametrized)
    result_updated_at = result.updated_at.strftime("%Y-%m-%d %H:%M:%S") #done these because they won't match because of the representation of the date in database. so we need to match the 2021-09-04 22:14:18 this format
    assert result.web_id == web_id
    assert result.name == name
    assert result.slug == slug
    assert result.description == description
    assert result.is_active == is_active
    assert result.created_at == created_at
    assert result.updated_at == updated_at