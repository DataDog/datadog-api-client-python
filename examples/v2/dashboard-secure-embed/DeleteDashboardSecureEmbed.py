"""
Delete a secure embed for a dashboard returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dashboard_secure_embed_api import DashboardSecureEmbedApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["delete_dashboard_secure_embed"] = True
with ApiClient(configuration) as api_client:
    api_instance = DashboardSecureEmbedApi(api_client)
    api_instance.delete_dashboard_secure_embed(
        dashboard_id="dashboard_id",
        token="token",
    )
