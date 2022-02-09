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

    # example passing only required values which don't have defaults set
    try:
        # Get hourly usage for Synthetics Browser Checks
        api_response = api_instance.get_usage_synthetics_browser(start_hr)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_synthetics_browser: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get hourly usage for Synthetics Browser Checks
        api_response = api_instance.get_usage_synthetics_browser(start_hr, end_hr=end_hr)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_synthetics_browser: %s\n" % e)
