"""
Delete GCP scan options returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agentless_scanning_api import AgentlessScanningApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AgentlessScanningApi(api_client)
    api_instance.delete_gcp_scan_options(
        project_id="company-project-id",
    )
