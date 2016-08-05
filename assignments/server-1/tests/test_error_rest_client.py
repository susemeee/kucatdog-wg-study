from . import (
    request_get, request_post, request_put, request_delete
)

def test_cookie_client_get_empty_returns_404(request_get):
    response = request_get('/cookie/999')
    assert response.status_code == 404


def test_cookie_client_put_empty_returns_404(request_put):
    response = request_put('/cookie/999')
    assert response.status_code == 404


def test_cookie_client_delete_empty_returns_404(request_delete):
    response = request_delete('/cookie/999')
    assert response.status_code == 404


def test_cookie_client_get_malformed_data_returns_400(request_get):
    response = request_get('/cookie/999', data='{')
    assert response.status_code == 400


def test_cookie_client_post_malformed_data_returns_400(request_post):
    response = request_post('/cookie/999', data='{')
    assert response.status_code == 400


def test_cookie_client_put_malformed_data_returns_400(request_put):
    response = request_put('/cookie/999', data='{')
    assert response.status_code == 400


def test_cookie_client_delete_malformed_data_returns_400(request_delete):
    response = request_delete('/cookie/999', data='{')
    assert response.status_code == 400


INVALID_FLAVOR_DATA = {'flavor': 'flowey', 'size': 15}
INVALID_SIZE_DATA = {'flavor': 'zombie', 'size': 999}


def test_cookie_client_post_invalid_flavor_data_returns_422(request_post):
    invalid_data = INVALID_FLAVOR_DATA
    response = request_post('/cookie/', data=invalid_data)
    assert response.status_code == 422


def test_cookie_client_post_invalid_size_data_returns_422(request_post):
    invalid_data = INVALID_SIZE_DATA
    response = request_post('/cookie/', data=invalid_data)
    assert response.status_code == 422


def _post_cookie(request_post):
    data = {'flavor': 'zombie', 'size': 20}
    response = request_post('/cookie/', data=data)

    return response.json()['id'], data


def test_cookie_client_put_invalid_flavor_data_returns_422(request_post, request_put):
    cookie_id, _ = _post_cookie(request_post)
    invalid_data = INVALID_FLAVOR_DATA
    response = request_put('/cookie/{}'.format(cookie_id), data=invalid_data)
    assert response.status_code == 422


def test_cookie_client_put_invalid_size_data_returns_422(request_post, request_put):
    cookie_id, _ = _post_cookie(request_post)
    invalid_data = INVALID_SIZE_DATA
    response = request_put('/cookie/{}'.format(cookie_id), data=invalid_data)
    assert response.status_code == 422
