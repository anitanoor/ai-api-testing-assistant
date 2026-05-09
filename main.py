import requests
from evaluator import evaluate_response


def call_api_endpoint(url, method="GET", data=None, headers=None):
    """
    Generic API caller
    """

    try:
        if method == "GET":
            response = requests.get(url, headers=headers)

        elif method == "POST":
            response = requests.post(url, json=data, headers=headers)

        else:
            return {
                "status": "error",
                "message": f"Unsupported method: {method}"
            }

        return {
            "status": "success",
            "status_code": response.status_code,
            "response": response.json(),
            "headers": dict(response.headers)
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


if __name__ == "__main__":

    url = "https://httpbin.org/get"

    result = call_api_endpoint(url)

    evaluation = evaluate_response(result)

    print("\nAPI Test Result:")
    print(result)

    print("\nAI Evaluation:")
    print(evaluation)