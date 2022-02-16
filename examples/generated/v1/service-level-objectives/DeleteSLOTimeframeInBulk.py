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
    body = SLOBulkDelete(
        key=[
            SLOTimeframe("30d"),
        ],
    )  # SLOBulkDelete | Delete multiple service level objective objects request body.

    # example passing only required values which don't have defaults set
    try:
        # Bulk Delete SLO Timeframes
        api_response = api_instance.delete_slo_timeframe_in_bulk(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceLevelObjectivesApi->delete_slo_timeframe_in_bulk: %s\n" % e)
