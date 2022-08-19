from rest_framework import status


def test_get_all_categories(api_client, category_with_multiple_children):
    endpoint = "/api/inventory/category/all/"
    response = api_client.get(path=endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == len(category_with_multiple_children)
