import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import security_monitoring_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["list_security_monitoring_signals"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_monitoring_api.SecurityMonitoringApi(api_client)
    filter_query = "security:attack status:high"  # str | The search query for security signals. (optional)
    filter_from = dateutil_parser('2019-01-02T09:42:36.320Z')  # datetime | The minimum timestamp for requested security signals. (optional)
    filter_to = dateutil_parser('2019-01-03T09:42:36.320Z')  # datetime | The maximum timestamp for requested security signals. (optional)
    sort = SecurityMonitoringSignalsSort("timestamp")  # SecurityMonitoringSignalsSort | The order of the security signals in results. (optional)
    page_cursor = "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="  # str | A list of results using the cursor provided in the previous query. (optional)
    page_limit = 25  # int | The maximum number of security signals in the response. (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a quick list of security signals
        api_response = api_instance.list_security_monitoring_signals(filter_query=filter_query, filter_from=filter_from, filter_to=filter_to, sort=sort, page_cursor=page_cursor, page_limit=page_limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecurityMonitoringApi->list_security_monitoring_signals: %s\n" % e)
