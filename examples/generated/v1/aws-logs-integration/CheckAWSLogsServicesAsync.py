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
    body = AWSLogsServicesRequest(
        account_id="1234567",
        services=["s3","elb","elbv2","cloudfront","redshift","lambda"],
    )  # AWSLogsServicesRequest | Check AWS Logs Async Services request body.

    # example passing only required values which don't have defaults set
    try:
        # Check permissions for log services
        api_response = api_instance.check_aws_logs_services_async(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AWSLogsIntegrationApi->check_aws_logs_services_async: %s\n" % e)
