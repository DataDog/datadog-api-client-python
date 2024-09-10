"""
List ASM Exclusion Filters returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.asm_exclusion_filters_api import ASMExclusionFiltersApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ASMExclusionFiltersApi(api_client)
    response = api_instance.list_asm_exclusion_filters()

    print(response)
