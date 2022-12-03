#we need to tell pytest to utilize that before we ran any test

#so everytime we ran pytest pytest will look this conftest file.

pytest_plugins = [
    "ecommerce.tests.selenium", #this is the path
    "ecommerce.tests.fixtures", #it includes the modules, just like url_pattern
]