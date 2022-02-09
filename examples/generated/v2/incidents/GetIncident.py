import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import incidents_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["get_incident"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = incidents_api.IncidentsApi(api_client)
    incident_id = "incident_id_example"  # str | The UUID of the incident.
    include = [
        IncidentRelatedObject("users"),
    ]  # [IncidentRelatedObject] | Specifies which types of related objects should be included in the response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the details of an incident
        api_response = api_instance.get_incident(incident_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IncidentsApi->get_incident: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the details of an incident
        api_response = api_instance.get_incident(incident_id, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IncidentsApi->get_incident: %s\n" % e)
