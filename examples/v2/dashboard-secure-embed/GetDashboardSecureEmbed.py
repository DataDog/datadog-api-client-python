"""
Get a secure embed for a dashboard returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dashboard_secure_embed_api import DashboardSecureEmbedApi

configuration = Configuration()
configuration.unstable_operations["get_dashboard_secure_embed"] = True
with ApiClient(configuration) as api_client:
    api_instance = DashboardSecureEmbedApi(api_client)
    response = api_instance.get_dashboard_secure_embed(
        dashboard_id="dashboard_id",
        token="token",
    )

    print(response)
