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
    )  # AWSAccount | AWS request object
    account_id = "account_id_example"  # str | Only return AWS accounts that matches this `account_id`. (optional)
    role_name = "role_name_example"  # str | Only return AWS accounts that match this `role_name`. Required if `account_id` is specified. (optional)
    access_key_id = "access_key_id_example"  # str | Only return AWS accounts that matches this `access_key_id`. Required if none of the other two options are specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an AWS integration
        api_response = api_instance.update_aws_account(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AWSIntegrationApi->update_aws_account: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an AWS integration
        api_response = api_instance.update_aws_account(body, account_id=account_id, role_name=role_name, access_key_id=access_key_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AWSIntegrationApi->update_aws_account: %s\n" % e)
