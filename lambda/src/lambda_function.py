# lambda_function.py

import json
import util.case_conversion_utils as case_conversion_utils


def lambda_handler(event, context):
    """
    Main Lambda function that routes events from API Gateway and manual executions.

    Parameters:
        event (dict): The event received by the Lambda function.
        context (object): The execution context of the Lambda function.

    Returns:
        dict: The HTTP response from the Lambda function.
    """
    if 'httpMethod' in event:
        event_snake_case = case_conversion_utils.convert_keys_to_snake_case(event)
        response = process_api_gateway_event(event_snake_case)
        return response
    else:
        response = process_manual_execution(event)
        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }


def process_api_gateway_event(event):
    """
    Processes the API Gateway event received by the Lambda function.

    Parameters:
        event (dict): The API Gateway event.

    Returns:
        dict: The HTTP response from the Lambda function.
    """
    http_method = event['httpMethod']
    path = event['path']
    query_string_parameters = event['queryStringParameters']

    response_body = {
        'httpMethod': http_method,
        'path': path,
        'queryParameters': query_string_parameters,
        'message': 'API Gateway event received and processed successfully'
    }

    return {
        'statusCode': 200,
        'body': json.dumps(response_body)
    }


def process_manual_execution(event):
    """
    Processes the execution received by the Lambda function.

    Parameters:
        event (dict): The execution event.

    Returns:
        dict: The response from the manual execution.
    """
    response_body = {
        'message': 'Manual execution received and processed successfully'
    }

    return response_body
