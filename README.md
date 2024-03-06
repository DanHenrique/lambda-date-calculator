# lambda-date-calculator

This Lambda function receives an object with date properties and formats the date into a desired format. The result can be returned as a JSON object or as a string.

## Usage

### Requirements

- AWS Lambda
- Python 3.x

### Input

The Lambda function expects to receive a JSON object with the following structure:

```json
{
  "date": "string",
  "desired_format": "string",
  "return_format": "string"
}
```

- `date` (string): The date you want to format.
- `desired_format` (string): The desired format for the date, following the syntax of the `datetime` library in Python.
- `return_format` (string): The format in which the result should be returned. Only accepts the options "json" or "dumps".

### Output

The Lambda will return the result in JSON format or as a string, depending on the preference.

The response from the Lambda (output) follows the following format:

```json
{
  "statusCode": 200,
  "body": {
    "date": "string",
    "format": "string"
  }
}
```

The `statusCode` field indicates the status of the response, and the `body` field contains an object with the attributes "date" and "format".

| Status Code | Description                                   |
|-------------|-----------------------------------------------|
| 200         | Success - OK                                  |
| 400         | Bad Request - Invalid Input                   |
| 500         | Internal Server Error - Something went wrong  |

## Example Usage

Assuming you have set up your Lambda function in AWS Lambda. You can invoke it using AWS CLI or any other available invocation method.

### Invocation via AWS CLI

```bash
aws lambda invoke --function-name YourLambdaFunctionName --payload '{"date": "2024-03-04", "desired_format": "%Y-%m-%d %H:%M:%S", "return_format": "json"}' response.json
```

## Contribution

Contributions are welcome! To contribute to this project, please follow these steps:

1. Fork the project
2. Create a branch with your feature (`git checkout -b feature/MyFeature`)
3. Commit your changes (`git commit -am 'Adding a new feature'`)
4. Push to the branch (`git push origin feature/MyFeature`)
5. Create a new Pull Request

## License

N/A
