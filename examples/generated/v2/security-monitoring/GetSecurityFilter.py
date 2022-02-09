import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import security_monitoring_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_monitoring_api.SecurityMonitoringApi(api_client)
    security_filter_id = "security_filter_id_example"  # str | The ID of the security filter.

    # example passing only required values which don't have defaults set
    try:
        # Get a security filter
        api_response = api_instance.get_security_filter(security_filter_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecurityMonitoringApi->get_security_filter: %s\n" % e)
