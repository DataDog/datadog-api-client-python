import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import service_accounts_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = service_accounts_api.ServiceAccountsApi(api_client)
    service_account_id = "00000000-0000-0000-0000-000000000000"  # str | The ID of the service account.
    app_key_id = "app_key_id_example"  # str | The ID of the application key.

    # example passing only required values which don't have defaults set
    try:
        # Delete an application key for this service account
        api_instance.delete_service_account_application_key(service_account_id, app_key_id)
    except ApiException as e:
        print("Exception when calling ServiceAccountsApi->delete_service_account_application_key: %s\n" % e)
