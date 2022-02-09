import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import aws_logs_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aws_logs_integration_api.AWSLogsIntegrationApi(api_client)
    body = AWSAccountAndLambdaRequest(
        account_id="1234567",
        lambda_arn="arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest",
    )  # AWSAccountAndLambdaRequest | Delete AWS Lambda ARN request body.

    # example passing only required values which don't have defaults set
    try:
        # Delete an AWS Logs integration
        api_response = api_instance.delete_aws_lambda_arn(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AWSLogsIntegrationApi->delete_aws_lambda_arn: %s\n" % e)
