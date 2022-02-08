import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import usage_metering_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["get_specified_daily_custom_reports"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    report_id = "report_id_example"  # str | Date of the report in the format `YYYY-MM-DD`.

    # example passing only required values which don't have defaults set
    try:
        # Get specified daily custom reports
        api_response = api_instance.get_specified_daily_custom_reports(report_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsageMeteringApi->get_specified_daily_custom_reports: %s\n" % e)
