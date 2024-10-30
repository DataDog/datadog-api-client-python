"""
Sets Domain Allowlist returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.domain_allowlist_api import DomainAllowlistApi
from datadog_api_client.v2.model.domain_allowlist import DomainAllowlist
from datadog_api_client.v2.model.domain_allowlist_attributes import DomainAllowlistAttributes
from datadog_api_client.v2.model.domain_allowlist_request import DomainAllowlistRequest
from datadog_api_client.v2.model.domain_allowlist_type import DomainAllowlistType

body = DomainAllowlistRequest(
    data=DomainAllowlist(
        attributes=DomainAllowlistAttributes(
            domains=[
                "@static-test-domain.test",
            ],
            enabled=False,
        ),
        type=DomainAllowlistType.DOMAIN_ALLOWLIST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DomainAllowlistApi(api_client)
    response = api_instance.patch_domain_allowlist(body=body)

    print(response)
