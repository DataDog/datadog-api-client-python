import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import usage_metering_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["get_hourly_usage_attribution"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    start_hr = dateutil_parser('1970-01-01T00:00:00.00Z')  # datetime | Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage beginning at this hour.
    usage_type = HourlyUsageAttributionUsageType("api_usage")  # HourlyUsageAttributionUsageType | Usage type to retrieve.
    end_hr = dateutil_parser('1970-01-01T00:00:00.00Z')  # datetime | Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage ending **before** this hour. (optional)
    next_record_id = "next_record_id_example"  # str | List following results with a next_record_id provided in the previous query. (optional)
    tag_breakdown_keys = "tag_breakdown_keys_example"  # str | Comma separated list of tags used to group usage. If no value is provided the usage will not be broken down by tags. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Hourly Usage Attribution
        api_response = api_instance.get_hourly_usage_attribution(start_hr, usage_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsageMeteringApi->get_hourly_usage_attribution: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Hourly Usage Attribution
        api_response = api_instance.get_hourly_usage_attribution(start_hr, usage_type, end_hr=end_hr, next_record_id=next_record_id, tag_breakdown_keys=tag_breakdown_keys)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsageMeteringApi->get_hourly_usage_attribution: %s\n" % e)
