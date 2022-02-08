import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import usage_metering_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["get_monthly_usage_attribution"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    start_month = dateutil_parser('1970-01-01T00:00:00.00Z')  # datetime | Datetime in ISO-8601 format, UTC, precise to month: `[YYYY-MM]` for usage beginning in this month. Maximum of 15 months ago.
    fields = MonthlyUsageAttributionSupportedMetrics("api_usage")  # MonthlyUsageAttributionSupportedMetrics | Comma-separated list of usage types to return, or `*` for all usage types.
    end_month = dateutil_parser('1970-01-01T00:00:00.00Z')  # datetime | Datetime in ISO-8601 format, UTC, precise to month: `[YYYY-MM]` for usage ending this month. (optional)
    sort_direction = UsageSortDirection("desc")  # UsageSortDirection | The direction to sort by: `[desc, asc]`. (optional)
    sort_name = MonthlyUsageAttributionSupportedMetrics("api_usage")  # MonthlyUsageAttributionSupportedMetrics | The field to sort by. (optional)
    tag_breakdown_keys = "tag_breakdown_keys_example"  # str | Comma separated list of tags used to group usage. If no value is provided the usage will not be broken down by tags. (optional)
    next_record_id = "next_record_id_example"  # str | List following results with a next_record_id provided in the previous query. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Monthly Usage Attribution
        api_response = api_instance.get_monthly_usage_attribution(start_month, fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsageMeteringApi->get_monthly_usage_attribution: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Monthly Usage Attribution
        api_response = api_instance.get_monthly_usage_attribution(start_month, fields, end_month=end_month, sort_direction=sort_direction, sort_name=sort_name, tag_breakdown_keys=tag_breakdown_keys, next_record_id=next_record_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsageMeteringApi->get_monthly_usage_attribution: %s\n" % e)
