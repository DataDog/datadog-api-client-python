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
    account_id = "account_id_example"  # str | Only return AWS accounts that matches this `account_id`. (optional)
    role_name = "role_name_example"  # str | Only return AWS accounts that matches this role_name. (optional)
    access_key_id = "access_key_id_example"  # str | Only return AWS accounts that matches this `access_key_id`. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all AWS integrations
        api_response = api_instance.list_aws_accounts(account_id=account_id, role_name=role_name, access_key_id=access_key_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AWSIntegrationApi->list_aws_accounts: %s\n" % e)
