import pytest
from fixture.application import Application


# лежит тут и полностью дублирует файл из корня на случай если надо запустить не всю папку, а конкретную страницу
# при изменении любого из - изменить оба
@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
