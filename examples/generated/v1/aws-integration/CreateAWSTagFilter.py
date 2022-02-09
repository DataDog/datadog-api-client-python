import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import aws_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aws_integration_api.AWSIntegrationApi(api_client)
    body = AWSTagFilterCreateRequest(
        account_id="1234567",
        namespace=AWSNamespace("elb"),
        tag_filter_str="prod*",
    )  # AWSTagFilterCreateRequest | Set an AWS tag filter using an `aws_account_identifier`, `namespace`, and filtering string. Namespace options are `application_elb`, `elb`, `lambda`, `network_elb`, `rds`, `sqs`, and `custom`.

    # example passing only required values which don't have defaults set
    try:
        # Set an AWS tag filter
        api_response = api_instance.create_aws_tag_filter(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AWSIntegrationApi->create_aws_tag_filter: %s\n" % e)
