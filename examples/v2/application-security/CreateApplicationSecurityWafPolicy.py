"""
Create a WAF Policy returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.application_security_api import ApplicationSecurityApi
from datadog_api_client.v2.model.application_security_policy_create_attributes import (
    ApplicationSecurityPolicyCreateAttributes,
)
from datadog_api_client.v2.model.application_security_policy_create_data import ApplicationSecurityPolicyCreateData
from datadog_api_client.v2.model.application_security_policy_create_request import (
    ApplicationSecurityPolicyCreateRequest,
)
from datadog_api_client.v2.model.application_security_policy_rule_override import ApplicationSecurityPolicyRuleOverride
from datadog_api_client.v2.model.application_security_policy_scope import ApplicationSecurityPolicyScope
from datadog_api_client.v2.model.application_security_policy_type import ApplicationSecurityPolicyType

body = ApplicationSecurityPolicyCreateRequest(
    data=ApplicationSecurityPolicyCreateData(
        attributes=ApplicationSecurityPolicyCreateAttributes(
            based_on="recommended",
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
    response = api_instance.create_application_security_waf_policy(body=body)

    print(response)
