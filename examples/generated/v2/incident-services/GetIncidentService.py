import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import incident_services_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["get_incident_service"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = incident_services_api.IncidentServicesApi(api_client)
    service_id = "service_id_example"  # str | The ID of the incident service.
    include = IncidentRelatedObject("users")  # IncidentRelatedObject | Specifies which types of related objects should be included in the response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of an incident service
        api_response = api_instance.get_incident_service(service_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IncidentServicesApi->get_incident_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of an incident service
        api_response = api_instance.get_incident_service(service_id, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IncidentServicesApi->get_incident_service: %s\n" % e)
