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
    page_size = 10  # int | Size for a given page. (optional) if omitted the server will use the default value of 10
    page_number = 0  # int | Specific page number to return. (optional) if omitted the server will use the default value of 0
    sort = ApplicationKeysSort("name")  # ApplicationKeysSort | Application key attribute used to sort results. Sort order is ascending by default. In order to specify a descending sort, prefix the attribute with a minus sign. (optional)
    filter = "filter_example"  # str | Filter application keys by the specified string. (optional)
    filter_created_at_start = "2020-11-24T18:46:21+00:00"  # str | Only include application keys created on or after the specified date. (optional)
    filter_created_at_end = "2020-11-24T18:46:21+00:00"  # str | Only include application keys created on or before the specified date. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List application keys for this service account
        api_response = api_instance.list_service_account_application_keys(service_account_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceAccountsApi->list_service_account_application_keys: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List application keys for this service account
        api_response = api_instance.list_service_account_application_keys(service_account_id, page_size=page_size, page_number=page_number, sort=sort, filter=filter, filter_created_at_start=filter_created_at_start, filter_created_at_end=filter_created_at_end)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceAccountsApi->list_service_account_application_keys: %s\n" % e)
