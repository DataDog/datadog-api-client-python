import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import service_level_objectives_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["get_slo_history"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = service_level_objectives_api.ServiceLevelObjectivesApi(api_client)
    slo_id = "slo_id_example"  # str | The ID of the service level objective object.
    from_ts = 1  # int | The `from` timestamp for the query window in epoch seconds.
    to_ts = 1  # int | The `to` timestamp for the query window in epoch seconds.
    target = 0  # float | The SLO target. If `target` is passed in, the response will include the remaining error budget and a timeframe value of `custom`. (optional)
    apply_correction = True  # bool | Defaults to `true`. If any SLO corrections are applied and this parameter is set to `false`, then the corrections will not be applied and the SLI values will not be affected. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get an SLO's history
        api_response = api_instance.get_slo_history(slo_id, from_ts, to_ts)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceLevelObjectivesApi->get_slo_history: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get an SLO's history
        api_response = api_instance.get_slo_history(slo_id, from_ts, to_ts, target=target, apply_correction=apply_correction)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceLevelObjectivesApi->get_slo_history: %s\n" % e)
