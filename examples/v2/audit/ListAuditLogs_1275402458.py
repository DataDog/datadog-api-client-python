"""
Get a list of Audit Logs events returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.audit_api import AuditApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AuditApi(api_client)
    items = api_instance.list_audit_logs_with_pagination(
        page_limit=2,
    )
    for item in items:
        print(item)
