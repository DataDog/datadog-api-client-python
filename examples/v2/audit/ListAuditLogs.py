"""
Get a list of Audit Logs events returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.audit_api import AuditApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AuditApi(api_client)
    response = api_instance.list_audit_logs()

    print(response)
