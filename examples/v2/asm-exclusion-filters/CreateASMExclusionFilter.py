"""
Create a ASM WAF Exclusion filter returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.asm_exclusion_filters_api import ASMExclusionFiltersApi
from datadog_api_client.v2.model.asm_exclusion_filter_create_attributes import ASMExclusionFilterCreateAttributes
from datadog_api_client.v2.model.asm_exclusion_filter_create_data import ASMExclusionFilterCreateData
from datadog_api_client.v2.model.asm_exclusion_filter_create_request import ASMExclusionFilterCreateRequest
from datadog_api_client.v2.model.asm_exclusion_filter_rule_target import ASMExclusionFilterRuleTarget
from datadog_api_client.v2.model.asm_exclusion_filter_rule_target_tags import ASMExclusionFilterRuleTargetTags
from datadog_api_client.v2.model.asm_exclusion_filter_scope import ASMExclusionFilterScope
from datadog_api_client.v2.model.asm_exclusion_filter_type import ASMExclusionFilterType

body = ASMExclusionFilterCreateRequest(
    data=ASMExclusionFilterCreateData(
        type=ASMExclusionFilterType.EXCLUSION_FILTER,
        attributes=ASMExclusionFilterCreateAttributes(
            description="my description",
            enabled=True,
            path_glob="*",
            rules_target=[
                ASMExclusionFilterRuleTarget(
                    tags=ASMExclusionFilterRuleTargetTags(
                        category="attack_attempt",
                        type="sql_injection",
                    ),
                ),
            ],
            scope=[
                ASMExclusionFilterScope(
                    env="staging",
                    service="container-resolver",
                ),
            ],
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ASMExclusionFiltersApi(api_client)
    response = api_instance.create_asm_exclusion_filter(body=body)

    print(response)
