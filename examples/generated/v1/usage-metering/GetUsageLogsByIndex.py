import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import usage_metering_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    start_hr = dateutil_parser('1970-01-01T00:00:00.00Z')  # datetime | Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour.
    end_hr = dateutil_parser('1970-01-01T00:00:00.00Z')  # datetime | Datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending **before** this hour. (optional)
    index_name = [
        "index_name_example",
    ]  # [str] | Comma-separated list of log index names. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get hourly usage for Logs by Index
        api_response = api_instance.get_usage_logs_by_index(start_hr)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_logs_by_index: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get hourly usage for Logs by Index
        api_response = api_instance.get_usage_logs_by_index(start_hr, end_hr=end_hr, index_name=index_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_logs_by_index: %s\n" % e)
