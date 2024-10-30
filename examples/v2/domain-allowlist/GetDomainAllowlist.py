"""
Get Domain Allowlist returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.domain_allowlist_api import DomainAllowlistApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DomainAllowlistApi(api_client)
    response = api_instance.get_domain_allowlist()

    print(response)
