def evaluate_response(response_data):
    """
    AI-style API response evaluator
    """

    score = 10

    feedback = []

    # Check response exists
    if "response" not in response_data:
        score -= 5
        feedback.append("Missing response payload")

    # Check status code
    if response_data.get("status_code") != 200:
        score -= 3
        feedback.append("Unexpected status code")

    # Check response structure
    response = response_data.get("response", {})

    if "url" not in response:
        score -= 1
        feedback.append("Missing URL field")

    if "headers" not in response:
        score -= 1
        feedback.append("Missing headers field")

    # Final success feedback
    if score == 10:
        feedback.append("API response passed all evaluation checks")

    return {
        "score": score,
        "feedback": feedback
    }