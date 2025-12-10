"""
Update a WAF Policy returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.application_security_api import ApplicationSecurityApi
from datadog_api_client.v2.model.application_security_policy_rule_override import ApplicationSecurityPolicyRuleOverride
from datadog_api_client.v2.model.application_security_policy_scope import ApplicationSecurityPolicyScope
from datadog_api_client.v2.model.application_security_policy_type import ApplicationSecurityPolicyType
from datadog_api_client.v2.model.application_security_policy_update_attributes import (
    ApplicationSecurityPolicyUpdateAttributes,
)
from datadog_api_client.v2.model.application_security_policy_update_data import ApplicationSecurityPolicyUpdateData
from datadog_api_client.v2.model.application_security_policy_update_request import (
    ApplicationSecurityPolicyUpdateRequest,
)

body = ApplicationSecurityPolicyUpdateRequest(
    data=ApplicationSecurityPolicyUpdateData(
        attributes=ApplicationSecurityPolicyUpdateAttributes(
            description="Policy applied to internal web applications.",
            is_default=False,
            name="Internal Network Policy",
            protection_presets=[
                "attack-tools",
            ],
            rules=[
                ApplicationSecurityPolicyRuleOverride(
                    blocking=False,
                    enabled=True,
                    id="rasp-001-002",
                ),
            ],
            scope=[
                ApplicationSecurityPolicyScope(
                    env="prod",
                    service="billing-service",
                ),
            ],
            version=0,
        ),
        type=ApplicationSecurityPolicyType.POLICY,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ApplicationSecurityApi(api_client)
    response = api_instance.update_application_security_waf_policy(policy_id="policy_id", body=body)

    print(response)
