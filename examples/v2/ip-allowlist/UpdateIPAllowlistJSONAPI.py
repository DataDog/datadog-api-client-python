"""
Update IP Allowlist returns "OK" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ip_allowlist_api import IPAllowlistApi
from datadog_api_client.v2.model.ip_allowlist_entry import IPAllowlistEntryJSON
from datadog_api_client.v2.model.ip_allowlist_update_request import IPAllowlistUpdateRequestJSON

body = IPAllowlistUpdateRequestJSON(
    entries=[
        IPAllowlistEntryJSON(
            note="Example-IP-Allowlist",
            cidr_block="127.0.0.1",
        ),
    ],
    enabled=False,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = IPAllowlistApi(api_client)
    response = api_instance.update_ip_allowlist(body=body)

    print(response)
