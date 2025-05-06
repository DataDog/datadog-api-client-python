"""
Resolve On-Call Page returns "Accepted." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_paging_api import OnCallPagingApi
from uuid import UUID

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallPagingApi(api_client)
    api_instance.resolve_on_call_page(
        page_id=UUID("15e74b8b-f865-48d0-bcc5-453323ed2c8f"),
    )
