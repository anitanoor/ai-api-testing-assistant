from main import call_api_endpoint


def test_get_request():

    url = "https://httpbin.org/get"

    result = call_api_endpoint(url)

    assert result["status"] == "success"
    assert result["status_code"] == 200
    assert "response" in result


def test_response_contains_url():

    url = "https://httpbin.org/get"

    result = call_api_endpoint(url)

    assert result["response"]["url"] == url


def test_invalid_method():

    url = "https://httpbin.org/get"

    result = call_api_endpoint(url, method="PUT")

    assert result["status"] == "error"