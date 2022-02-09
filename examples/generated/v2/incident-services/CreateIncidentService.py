import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import incident_services_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["create_incident_service"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = incident_services_api.IncidentServicesApi(api_client)
    body = IncidentServiceCreateRequest(
        data=IncidentServiceCreateData(
            attributes=IncidentServiceCreateAttributes(
                name="an example service name",
            ),
            type=IncidentServiceType("services"),
        ),
    )  # IncidentServiceCreateRequest | Incident Service Payload.

    # example passing only required values which don't have defaults set
    try:
        # Create a new incident service
        api_response = api_instance.create_incident_service(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IncidentServicesApi->create_incident_service: %s\n" % e)
