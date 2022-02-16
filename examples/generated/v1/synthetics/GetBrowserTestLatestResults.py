import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    public_id = "public_id_example"  # str | The public ID of the browser test for which to search results for.
    from_ts = 1  # int | Timestamp in milliseconds from which to start querying results. (optional)
    to_ts = 1  # int | Timestamp in milliseconds up to which to query results. (optional)
    probe_dc = [
        "probe_dc_example",
    ]  # [str] | Locations for which to query results. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a browser test's latest results summaries
        api_response = api_instance.get_browser_test_latest_results(public_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SyntheticsApi->get_browser_test_latest_results: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a browser test's latest results summaries
        api_response = api_instance.get_browser_test_latest_results(public_id, from_ts=from_ts, to_ts=to_ts, probe_dc=probe_dc)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SyntheticsApi->get_browser_test_latest_results: %s\n" % e)
