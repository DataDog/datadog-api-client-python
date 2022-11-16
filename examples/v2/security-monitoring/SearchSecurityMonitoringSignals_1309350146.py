"""
Get a list of security signals returns "OK" response with pagination
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
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

body = SecurityMonitoringSignalListRequest(
    filter=SecurityMonitoringSignalListRequestFilter(
        _from=(datetime.now() + relativedelta(minutes=-15)),
        query="security:attack status:high",
        to=datetime.now(),
    ),
    page=SecurityMonitoringSignalListRequestPage(
        limit=2,
    ),
    sort=SecurityMonitoringSignalsSort.TIMESTAMP_ASCENDING,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    items = api_instance.search_security_monitoring_signals_with_pagination(body=body)
    for item in items:
        print(item)
