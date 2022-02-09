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
    start_month = dateutil_parser('1970-01-01T00:00:00.00Z')  # datetime | Datetime in ISO-8601 format, UTC, precise to month: `[YYYY-MM]` for usage beginning in this month. Maximum of 15 months ago.
    end_month = dateutil_parser('1970-01-01T00:00:00.00Z')  # datetime | Datetime in ISO-8601 format, UTC, precise to month: `[YYYY-MM]` for usage ending this month. (optional)
    include_org_details = True  # bool | Include usage summaries for each sub-org. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get usage across your multi-org account
        api_response = api_instance.get_usage_summary(start_month)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_summary: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get usage across your multi-org account
        api_response = api_instance.get_usage_summary(start_month, end_month=end_month, include_org_details=include_org_details)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_summary: %s\n" % e)
