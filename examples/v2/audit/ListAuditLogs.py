"""
Get a list of Audit Logs events returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.audit_api import AuditApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = AuditApi(api_client)
    response = api_instance.list_audit_logs()

    print(response)
