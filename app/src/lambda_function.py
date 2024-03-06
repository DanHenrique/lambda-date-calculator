import json
from src.util.date_utils import convert_date


def lambda_handler(event, context):
    '''
     Main Lambda function that routes events from API Gateway and manual executions.

    Parameters:
        event (dict): The event received by the Lambda function.
            - 'date' (str): The date that needs to be converted.
            - 'format' (str): The desired date format.
            - 'return_format' (str, None): The format of the return body.
                Defaults to 'json'. Acceptable values are 'json' or 'dumps'.
        context (dict): The execution context of the Lambda function.

    Returns:
        dict: The HTTP response from the Lambda function.
            - 'statusCode' (int): The status code response from the lambda.
            - 'body' (str): The actual result from the lambda function.
    '''
    return_format = event.get('return_format', 'json')  # Obtém o formato de retorno do corpo

    try:
        converted_date = convert_date(date_iso8601=event['date'], desired_format=event.get('desired_format', None))

        return {
            'statusCode': 200,
            'body': converted_date if return_format == 'json' else json.dumps(converted_date)
        }
    except (ValueError, KeyError) as ve:
        # Retorna um objeto JSON de erro com status 400 (BadRequest)
        err = {
            'error': str(ve)
        }
        error_response = {
            'statusCode': 400,
            'body': err if return_format == 'json' else json.dumps(err)
        }
        return error_response
    except Exception as e:
        # Retorna um objeto JSON de erro genérico com status 500
        err = {
            'error': str(e)
        }
        error_response = {
            'statusCode': 500,
            'body': e if return_format == 'json' else json.dumps(e)
        }
        return error_response
