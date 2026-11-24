"""
Update the outreach mode returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.bits_security_analyst_api import BitsSecurityAnalystApi
from datadog_api_client.v2.model.security_agent_outreach_mode import SecurityAgentOutreachMode
from datadog_api_client.v2.model.security_agent_outreach_mode_attributes import SecurityAgentOutreachModeAttributes
from datadog_api_client.v2.model.security_agent_outreach_mode_update_data import SecurityAgentOutreachModeUpdateData
from datadog_api_client.v2.model.security_agent_outreach_mode_update_request import (
    SecurityAgentOutreachModeUpdateRequest,
)
from datadog_api_client.v2.model.security_agent_outreach_policy_type import SecurityAgentOutreachPolicyType

body = SecurityAgentOutreachModeUpdateRequest(
    data=SecurityAgentOutreachModeUpdateData(
        attributes=SecurityAgentOutreachModeAttributes(
            mode=SecurityAgentOutreachMode.AUTOMATED,
        ),
        type=SecurityAgentOutreachPolicyType.OUTREACH_POLICY,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_security_agent_outreach_mode"] = True
with ApiClient(configuration) as api_client:
    api_instance = BitsSecurityAnalystApi(api_client)
    response = api_instance.update_security_agent_outreach_mode(body=body)

    print(response)
