import json
from src.Function.handler import lambda_handler

def test_lambda_handler_returns_message():
    event = {"name": "UnitTestApp"}
    context = {}
    response = lambda_handler(event, context)

    assert response["statusCode"] == 200
    body = json.loads(response["body"])
    assert body["message"] == "Hello, UnitTestApp!"
