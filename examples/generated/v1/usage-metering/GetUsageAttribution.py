import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import usage_metering_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["get_usage_attribution"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    start_month = dateutil_parser('1970-01-01T00:00:00.00Z')  # datetime | Datetime in ISO-8601 format, UTC, precise to month: `[YYYY-MM]` for usage beginning in this month. Maximum of 15 months ago.
    fields = UsageAttributionSupportedMetrics("custom_timeseries_usage")  # UsageAttributionSupportedMetrics | Comma-separated list of usage types to return, or `*` for all usage types.
    end_month = dateutil_parser('1970-01-01T00:00:00.00Z')  # datetime | Datetime in ISO-8601 format, UTC, precise to month: `[YYYY-MM]` for usage ending this month. (optional)
    sort_direction = UsageSortDirection("desc")  # UsageSortDirection | The direction to sort by: `[desc, asc]`. (optional)
    sort_name = UsageAttributionSort("custom_timeseries_usage")  # UsageAttributionSort | The field to sort by. (optional)
    include_descendants = False  # bool | Include child org usage in the response. Defaults to false. (optional) if omitted the server will use the default value of False
    offset = 0  # int | Number of records to skip before beginning to return. (optional) if omitted the server will use the default value of 0
    limit = 5000  # int | Maximum number of records to be returned. (optional) if omitted the server will use the default value of 5000

    # example passing only required values which don't have defaults set
    try:
        # Get Usage Attribution
        api_response = api_instance.get_usage_attribution(start_month, fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_attribution: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Usage Attribution
        api_response = api_instance.get_usage_attribution(start_month, fields, end_month=end_month, sort_direction=sort_direction, sort_name=sort_name, include_descendants=include_descendants, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_attribution: %s\n" % e)
