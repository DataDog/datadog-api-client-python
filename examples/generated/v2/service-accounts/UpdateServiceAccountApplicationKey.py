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
    body = ApplicationKeyUpdateRequest(
        data=ApplicationKeyUpdateData(
            attributes=ApplicationKeyUpdateAttributes(
                name="Application Key for managing dashboards",
                scopes=["dashboards_read","dashboards_write","dashboards_public_share"],
            ),
            id="00112233-4455-6677-8899-aabbccddeeff",
            type=ApplicationKeysType("application_keys"),
        ),
    )  # ApplicationKeyUpdateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Edit an application key for this service account
        api_response = api_instance.update_service_account_application_key(service_account_id, app_key_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceAccountsApi->update_service_account_application_key: %s\n" % e)
