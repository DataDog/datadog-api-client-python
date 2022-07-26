"""
Get a quick list of security signals returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    items = api_instance.list_security_monitoring_signals_with_pagination(
        page_limit=2,
    )
    for item in items:
        print(item)
