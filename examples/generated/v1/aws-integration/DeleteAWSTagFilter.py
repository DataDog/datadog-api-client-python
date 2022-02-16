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
    body = AWSTagFilterDeleteRequest(
        account_id="FAKEAC0FAKEAC2FAKEAC",
        namespace=AWSNamespace("elb"),
    )  # AWSTagFilterDeleteRequest | Delete a tag filtering entry for a given AWS account and `dd-aws` namespace.

    # example passing only required values which don't have defaults set
    try:
        # Delete a tag filtering entry
        api_response = api_instance.delete_aws_tag_filter(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AWSIntegrationApi->delete_aws_tag_filter: %s\n" % e)
