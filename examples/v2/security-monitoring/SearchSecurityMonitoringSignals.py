"""
Get a list of security signals returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_signal_list_request import SecurityMonitoringSignalListRequest
from datadog_api_client.v2.model.security_monitoring_signal_list_request_filter import (
    SecurityMonitoringSignalListRequestFilter,
)
from datadog_api_client.v2.model.security_monitoring_signal_list_request_page import (
    SecurityMonitoringSignalListRequestPage,
)
from datadog_api_client.v2.model.security_monitoring_signals_sort import SecurityMonitoringSignalsSort
from datetime import datetime
from dateutil.tz import tzutc

body = SecurityMonitoringSignalListRequest(
    filter=SecurityMonitoringSignalListRequestFilter(
        _from=datetime(2019, 1, 2, 9, 42, 36, 320000, tzinfo=tzutc()),
        query="security:attack status:high",
        to=datetime(2019, 1, 3, 9, 42, 36, 320000, tzinfo=tzutc()),
    ),
    page=SecurityMonitoringSignalListRequestPage(
        cursor="eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==",
        limit=25,
    ),
    sort=SecurityMonitoringSignalsSort.TIMESTAMP_ASCENDING,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.search_security_monitoring_signals(body=body)

    print(response)
