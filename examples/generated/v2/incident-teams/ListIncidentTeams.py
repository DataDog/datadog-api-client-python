import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import incident_teams_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["list_incident_teams"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = incident_teams_api.IncidentTeamsApi(api_client)
    include = IncidentRelatedObject("users")  # IncidentRelatedObject | Specifies which types of related objects should be included in the response. (optional)
    page_size = 10  # int | Size for a given page. (optional) if omitted the server will use the default value of 10
    page_offset = 0  # int | Specific offset to use as the beginning of the returned page. (optional) if omitted the server will use the default value of 0
    filter = "ExampleTeamName"  # str | A search query that filters teams by name. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of all incident teams
        api_response = api_instance.list_incident_teams(include=include, page_size=page_size, page_offset=page_offset, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IncidentTeamsApi->list_incident_teams: %s\n" % e)
