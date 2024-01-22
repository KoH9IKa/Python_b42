import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
# лежит тут и полностью дублирует файл из папки test на случай если надо запустить не всю папку, а конкретную страницу
# при изменении любого из - изменить оба
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
