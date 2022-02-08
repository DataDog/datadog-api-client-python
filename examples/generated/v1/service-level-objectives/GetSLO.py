import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import service_level_objectives_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = service_level_objectives_api.ServiceLevelObjectivesApi(api_client)
    slo_id = "slo_id_example"  # str | The ID of the service level objective object.
    with_configured_alert_ids = True  # bool | Get the IDs of SLO monitors that reference this SLO. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get an SLO's details
        api_response = api_instance.get_slo(slo_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceLevelObjectivesApi->get_slo: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get an SLO's details
        api_response = api_instance.get_slo(slo_id, with_configured_alert_ids=with_configured_alert_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceLevelObjectivesApi->get_slo: %s\n" % e)
