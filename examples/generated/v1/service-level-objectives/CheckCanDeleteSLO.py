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
    ids = "id1, id2, id3"  # str | A comma separated list of the IDs of the service level objectives objects.

    # example passing only required values which don't have defaults set
    try:
        # Check if SLOs can be safely deleted
        api_response = api_instance.check_can_delete_slo(ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceLevelObjectivesApi->check_can_delete_slo: %s\n" % e)
