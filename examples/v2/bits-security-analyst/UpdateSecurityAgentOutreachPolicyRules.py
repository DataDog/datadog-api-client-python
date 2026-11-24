"""
Update outreach policy rules returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.bits_security_analyst_api import BitsSecurityAnalystApi
from datadog_api_client.v2.model.security_agent_outreach_rule_update import SecurityAgentOutreachRuleUpdate
from datadog_api_client.v2.model.security_agent_outreach_rules_update_attributes import (
    SecurityAgentOutreachRulesUpdateAttributes,
)
from datadog_api_client.v2.model.security_agent_outreach_rules_update_request import (
    SecurityAgentOutreachRulesUpdateRequest,
)
from datadog_api_client.v2.model.security_agent_outreach_rules_update_request_data import (
    SecurityAgentOutreachRulesUpdateRequestData,
)
from datadog_api_client.v2.model.security_agent_outreach_rules_update_type import SecurityAgentOutreachRulesUpdateType

body = SecurityAgentOutreachRulesUpdateRequest(
    data=SecurityAgentOutreachRulesUpdateRequestData(
        attributes=SecurityAgentOutreachRulesUpdateAttributes(
            rules=[
                SecurityAgentOutreachRuleUpdate(
                    is_enabled=True,
                    rule_id="abc-def-ghi",
                ),
            ],
        ),
        type=SecurityAgentOutreachRulesUpdateType.OUTREACH_POLICY_RULES_UPDATE,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_security_agent_outreach_policy_rules"] = True
with ApiClient(configuration) as api_client:
    api_instance = BitsSecurityAnalystApi(api_client)
    response = api_instance.update_security_agent_outreach_policy_rules(body=body)

    print(response)
