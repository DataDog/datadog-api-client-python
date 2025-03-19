"""
Create a WAF exclusion filter returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.application_security_api import ApplicationSecurityApi
from datadog_api_client.v2.model.application_security_waf_exclusion_filter_create_attributes import (
    ApplicationSecurityWafExclusionFilterCreateAttributes,
)
from datadog_api_client.v2.model.application_security_waf_exclusion_filter_create_data import (
    ApplicationSecurityWafExclusionFilterCreateData,
)
from datadog_api_client.v2.model.application_security_waf_exclusion_filter_create_request import (
    ApplicationSecurityWafExclusionFilterCreateRequest,
)
from datadog_api_client.v2.model.application_security_waf_exclusion_filter_rules_target import (
    ApplicationSecurityWafExclusionFilterRulesTarget,
)
from datadog_api_client.v2.model.application_security_waf_exclusion_filter_rules_target_tags import (
    ApplicationSecurityWafExclusionFilterRulesTargetTags,
)
from datadog_api_client.v2.model.application_security_waf_exclusion_filter_scope import (
    ApplicationSecurityWafExclusionFilterScope,
)
from datadog_api_client.v2.model.application_security_waf_exclusion_filter_type import (
    ApplicationSecurityWafExclusionFilterType,
)

body = ApplicationSecurityWafExclusionFilterCreateRequest(
    data=ApplicationSecurityWafExclusionFilterCreateData(
        attributes=ApplicationSecurityWafExclusionFilterCreateAttributes(
            description="Exclude false positives on a path",
            enabled=True,
            parameters=[
                "list.search.query",
            ],
            path_glob="/accounts/*",
            rules_target=[
                ApplicationSecurityWafExclusionFilterRulesTarget(
                    tags=ApplicationSecurityWafExclusionFilterRulesTargetTags(
                        category="attack_attempt",
                        type="lfi",
                    ),
                ),
            ],
            scope=[
                ApplicationSecurityWafExclusionFilterScope(
                    env="www",
                    service="prod",
                ),
            ],
        ),
        type=ApplicationSecurityWafExclusionFilterType.EXCLUSION_FILTER,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ApplicationSecurityApi(api_client)
    response = api_instance.create_application_security_waf_exclusion_filter(body=body)

    print(response)
