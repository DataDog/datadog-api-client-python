import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import usage_metering_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["get_monthly_custom_reports"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    page_size = 1  # int | The number of files to return in the response `[default=60].` (optional)
    page_number = 1  # int | The identifier of the first page to return. This parameter is used for the pagination feature `[default=0]`. (optional)
    sort_dir = UsageSortDirection("desc")  # UsageSortDirection | The direction to sort by: `[desc, asc]`. (optional)
    sort = UsageSort("start_date")  # UsageSort | The field to sort by: `[computed_on, size, start_date, end_date]`. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the list of available monthly custom reports
        api_response = api_instance.get_monthly_custom_reports(page_size=page_size, page_number=page_number, sort_dir=sort_dir, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsageMeteringApi->get_monthly_custom_reports: %s\n" % e)
