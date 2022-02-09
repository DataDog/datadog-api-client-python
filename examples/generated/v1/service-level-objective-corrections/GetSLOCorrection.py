import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import service_level_objective_corrections_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["get_slo_correction"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = service_level_objective_corrections_api.ServiceLevelObjectiveCorrectionsApi(api_client)
    slo_correction_id = "slo_correction_id_example"  # str | The ID of the SLO correction object.

    # example passing only required values which don't have defaults set
    try:
        # Get an SLO correction for an SLO
        api_response = api_instance.get_slo_correction(slo_correction_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceLevelObjectiveCorrectionsApi->get_slo_correction: %s\n" % e)
