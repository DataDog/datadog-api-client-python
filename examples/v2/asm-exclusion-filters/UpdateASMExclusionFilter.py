"""
Update a ASM Exclusion filter returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.asm_exclusion_filters_api import ASMExclusionFiltersApi
from datadog_api_client.v2.model.asm_exclusion_filter_rule_target import ASMExclusionFilterRuleTarget
from datadog_api_client.v2.model.asm_exclusion_filter_rule_target_tags import ASMExclusionFilterRuleTargetTags
from datadog_api_client.v2.model.asm_exclusion_filter_scope import ASMExclusionFilterScope
from datadog_api_client.v2.model.asm_exclusion_filter_type import ASMExclusionFilterType
from datadog_api_client.v2.model.asm_exclusion_filter_update_attributes import ASMExclusionFilterUpdateAttributes
from datadog_api_client.v2.model.asm_exclusion_filter_update_data import ASMExclusionFilterUpdateData
from datadog_api_client.v2.model.asm_exclusion_filter_update_request import ASMExclusionFilterUpdateRequest

body = ASMExclusionFilterUpdateRequest(
    data=ASMExclusionFilterUpdateData(
        attributes=ASMExclusionFilterUpdateAttributes(
            description="My Exclusion filter",
            enabled=True,
            ip_list=[
                "127.0.0.1",
            ],
            path_glob="/lfi_include/*",
            rules_target=[
                ASMExclusionFilterRuleTarget(
                    tags=ASMExclusionFilterRuleTargetTags(
                        category="attack_attempt",
                        type="lfi",
                    ),
                ),
            ],
            scope=[
                ASMExclusionFilterScope(
                    env="dd-appsec-php-support",
                    service="anil-php-weblog",
                ),
            ],
        ),
        id="3dd-0uc-h1s",
        type=ASMExclusionFilterType.EXCLUSION_FILTER,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ASMExclusionFiltersApi(api_client)
    response = api_instance.update_asm_exclusion_filter(exclusion_filter_id="exclusion_filter_id", body=body)

    print(response)
