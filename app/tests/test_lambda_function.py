# test_lambda_function.py
import json
import unittest
from src.lambda_function import lambda_handler


class TestLambdaHandler(unittest.TestCase):
    def test_handler_json_return(self):
        # Test case for process_api_gateway_event
        event = {
            'date': '2000-10-31T01:30:00.000',
            'desired_format': '%Y-%m-%d %H:%M:%S',
            'return_format': 'json'
        }
        context = {}
        expected_response = {
            'statusCode': 200,
            'body': {
                'date': '2000-10-31 01:30:00',
                'format': '%Y-%m-%d %H:%M:%S'
            }
        }
        # Testing the return format when sent in the input event
        self.assertEqual(lambda_handler(event, context), expected_response)
        # Testing the return format when not sent in the input event
        event.pop('return_format')
        self.assertEqual(lambda_handler(event, context), expected_response)

    def test_handler_dumps_return(self):
        # Test case for process_api_gateway_event
        event = {
            'date': '2000-10-31T01:30:00.000',
            'desired_format': '%Y-%m-%d %H:%M:%S',
            'return_format': 'dumps'
        }
        context = {}
        expected_response = {
            'statusCode': 200,
            'body': json.dumps({
                'date': '2000-10-31 01:30:00',
                'format': '%Y-%m-%d %H:%M:%S'
            })
        }

        response = lambda_handler(event, context)
        self.assertEqual(response, expected_response)


if __name__ == '__main__':
    unittest.main()
