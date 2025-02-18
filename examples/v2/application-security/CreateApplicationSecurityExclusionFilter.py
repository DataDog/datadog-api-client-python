"""
Create an Application Security exclusion filter returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.application_security_api import ApplicationSecurityApi
from datadog_api_client.v2.model.application_security_exclusion_filter_attributes import (
    ApplicationSecurityExclusionFilterAttributes,
)
from datadog_api_client.v2.model.application_security_exclusion_filter_on_match import (
    ApplicationSecurityExclusionFilterOnMatch,
)
from datadog_api_client.v2.model.application_security_exclusion_filter_request import (
    ApplicationSecurityExclusionFilterRequest,
)
from datadog_api_client.v2.model.application_security_exclusion_filter_resource import (
    ApplicationSecurityExclusionFilterResource,
)
from datadog_api_client.v2.model.application_security_exclusion_filter_rules_target import (
    ApplicationSecurityExclusionFilterRulesTarget,
)
from datadog_api_client.v2.model.application_security_exclusion_filter_rules_target_tags import (
    ApplicationSecurityExclusionFilterRulesTargetTags,
)
from datadog_api_client.v2.model.application_security_exclusion_filter_scope import (
    ApplicationSecurityExclusionFilterScope,
)
from datadog_api_client.v2.model.application_security_exclusion_filter_type import (
    ApplicationSecurityExclusionFilterType,
)

body = ApplicationSecurityExclusionFilterRequest(
    data=ApplicationSecurityExclusionFilterResource(
        attributes=ApplicationSecurityExclusionFilterAttributes(
            description="Exclude false positives on a path",
            enabled=True,
            ip_list=[
                "198.51.100.72",
            ],
            on_match=ApplicationSecurityExclusionFilterOnMatch.MONITOR,
            parameters=[
                "list.search.query",
            ],
            path_glob="/accounts/*",
            rules_target=[
                ApplicationSecurityExclusionFilterRulesTarget(
                    rule_id="dog-913-009",
                    tags=ApplicationSecurityExclusionFilterRulesTargetTags(
                        category="attack_attempt",
                        type="lfi",
                    ),
                ),
            ],
            scope=[
                ApplicationSecurityExclusionFilterScope(
                    env="www",
                    service="prod",
                ),
            ],
        ),
        type=ApplicationSecurityExclusionFilterType.EXCLUSION_FILTER,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ApplicationSecurityApi(api_client)
    response = api_instance.create_application_security_exclusion_filter(body=body)

    print(response)
