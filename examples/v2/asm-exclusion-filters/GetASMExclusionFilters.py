"""
Get a specific ASM Exclusion Filter returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.asm_exclusion_filters_api import ASMExclusionFiltersApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ASMExclusionFiltersApi(api_client)
    response = api_instance.get_asm_exclusion_filters(
        exclusion_filter_id="exclusion_filter_id",
    )

    print(response)
