"""
Update IP Allowlist returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ip_allowlist_api import IPAllowlistApi
from datadog_api_client.v2.model.ip_allowlist_attributes import IPAllowlistAttributes
from datadog_api_client.v2.model.ip_allowlist_data import IPAllowlistData
from datadog_api_client.v2.model.ip_allowlist_entry import IPAllowlistEntry
from datadog_api_client.v2.model.ip_allowlist_entry_attributes import IPAllowlistEntryAttributes
from datadog_api_client.v2.model.ip_allowlist_entry_data import IPAllowlistEntryData
from datadog_api_client.v2.model.ip_allowlist_entry_type import IPAllowlistEntryType
from datadog_api_client.v2.model.ip_allowlist_type import IPAllowlistType
from datadog_api_client.v2.model.ip_allowlist_update_request import IPAllowlistUpdateRequest

body = IPAllowlistUpdateRequest(
    data=IPAllowlistData(
        attributes=IPAllowlistAttributes(
            entries=[
                IPAllowlistEntry(
                    data=IPAllowlistEntryData(
                        attributes=IPAllowlistEntryAttributes(
                            note="Example-IP-Allowlist",
                            cidr_block="127.0.0.1",
                        ),
                        type=IPAllowlistEntryType.IP_ALLOWLIST_ENTRY,
                    ),
                ),
            ],
            enabled=False,
        ),
        type=IPAllowlistType.IP_ALLOWLIST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = IPAllowlistApi(api_client)
    response = api_instance.update_ip_allowlist(body=body)

    print(response)
