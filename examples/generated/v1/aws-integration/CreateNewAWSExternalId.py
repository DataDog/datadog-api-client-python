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
    body = AWSAccount(
        access_key_id="access_key_id_example",
        account_id="1234567",
        account_specific_namespace_rules={
            "key": True,
        },
        cspm_resource_collection_enabled=True,
        excluded_regions=["us-east-1","us-west-2"],
        filter_tags=["<KEY>:<VALUE>"],
        host_tags=["<KEY>:<VALUE>"],
        metrics_collection_enabled=False,
        resource_collection_enabled=True,
        role_name="DatadogAWSIntegrationRole",
        secret_access_key="secret_access_key_example",
    )  # AWSAccount | Your Datadog role delegation name. For more information about your AWS account Role name, see the [Datadog AWS integration configuration info](https://docs.datadoghq.com/integrations/amazon_web_services/#setup).

    # example passing only required values which don't have defaults set
    try:
        # Generate a new external ID
        api_response = api_instance.create_new_aws_external_id(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AWSIntegrationApi->create_new_aws_external_id: %s\n" % e)
