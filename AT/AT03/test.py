import pytest
from main import get_random_cat_image

# Функция, имитирующая соединение с thecatapi и проверяющая
# работу функции get_random_cat_image когда соединение прошло успешно
def test_get_random_cat_image(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {
            "id": "abc123",
            "url": "https://cdn2.thecatapi.com/images/abc123.jpg",
            "width": 800,
            "height": 600
        }
    ]

    user_data = get_random_cat_image()

    assert user_data == "https://cdn2.thecatapi.com/images/abc123.jpg"


# Функция, тестирующая работу функции get_random_cat_image в случае,
# когда соединение с thecatapi вызвало ошибку 404
def test_get_random_cat_image_with_error(mocker):
   mock_get = mocker.patch('main.requests.get')
   mock_get.return_value.status_code = 404

   user_data = get_random_cat_image()

   assert user_data == None