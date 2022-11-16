"""
Search Audit Logs events returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.audit_api import AuditApi
from datadog_api_client.v2.model.audit_logs_query_filter import AuditLogsQueryFilter
from datadog_api_client.v2.model.audit_logs_query_options import AuditLogsQueryOptions
from datadog_api_client.v2.model.audit_logs_query_page_options import AuditLogsQueryPageOptions
from datadog_api_client.v2.model.audit_logs_search_events_request import AuditLogsSearchEventsRequest
from datadog_api_client.v2.model.audit_logs_sort import AuditLogsSort

body = AuditLogsSearchEventsRequest(
    filter=AuditLogsQueryFilter(
        _from="now-15m",
        to="now",
    ),
    options=AuditLogsQueryOptions(
        timezone="GMT",
    ),
    page=AuditLogsQueryPageOptions(
        limit=2,
    ),
    sort=AuditLogsSort.TIMESTAMP_ASCENDING,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AuditApi(api_client)
    items = api_instance.search_audit_logs_with_pagination(body=body)
    for item in items:
        print(item)
