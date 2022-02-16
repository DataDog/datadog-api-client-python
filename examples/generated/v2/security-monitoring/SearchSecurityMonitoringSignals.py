import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import security_monitoring_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["search_security_monitoring_signals"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_monitoring_api.SecurityMonitoringApi(api_client)
    body = SecurityMonitoringSignalListRequest(
        filter=SecurityMonitoringSignalListRequestFilter(
            _from=dateutil_parser('2019-01-02T09:42:36.32Z'),
            query="security:attack status:high",
            to=dateutil_parser('2019-01-03T09:42:36.32Z'),
        ),
        page=SecurityMonitoringSignalListRequestPage(
            cursor="eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==",
            limit=25,
        ),
        sort=SecurityMonitoringSignalsSort("timestamp"),
    )  # SecurityMonitoringSignalListRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of security signals
        api_response = api_instance.search_security_monitoring_signals(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecurityMonitoringApi->search_security_monitoring_signals: %s\n" % e)
