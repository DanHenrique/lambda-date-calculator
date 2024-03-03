# test_lambda_function.py

import unittest
from src.lambda_function import lambda_handler, process_api_gateway_event, process_manual_execution


class TestLambdaHandler(unittest.TestCase):
    def test_process_api_gateway_event(self):
        # Test case for process_api_gateway_event
        event = {'httpMethod': 'GET', 'path': '/test', 'queryStringParameters': {'param1': 'value1'}}
        expected_response = {
            'statusCode': 200,
            'body': '{"httpMethod": "GET", "path": "/test", "queryParameters": {"param1": "value1"}, "message": "API Gateway event received and processed successfully"}'
        }
        self.assertEqual(process_api_gateway_event(event), expected_response)

    def test_process_manual_execution(self):
        # Test case for process_manual_execution
        event = {'key': 'value'}
        expected_response = {'message': 'Manual execution received and processed successfully'}
        self.assertEqual(process_manual_execution(event), expected_response)

    def test_lambda_handler_add(self):
        event = {'x': 2, 'y': 3, 'operation': 'add'}
        result = lambda_handler(event, None)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
