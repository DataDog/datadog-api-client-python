import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import organizations_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organizations_api.OrganizationsApi(api_client)
    body = OrganizationCreateBody(
        billing=OrganizationBilling(
            type="type_example",
        ),
        name="New child org",
        subscription=OrganizationSubscription(
            type="type_example",
        ),
    )  # OrganizationCreateBody | Organization object that needs to be created

    # example passing only required values which don't have defaults set
    try:
        # Create a child organization
        api_response = api_instance.create_child_org(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganizationsApi->create_child_org: %s\n" % e)
