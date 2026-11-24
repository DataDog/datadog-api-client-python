"""
Add an allowed outreach domain returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.bits_security_analyst_api import BitsSecurityAnalystApi
from datadog_api_client.v2.model.security_agent_outreach_domain_add_request import SecurityAgentOutreachDomainAddRequest
from datadog_api_client.v2.model.security_agent_outreach_domain_add_request_data import (
    SecurityAgentOutreachDomainAddRequestData,
)
from datadog_api_client.v2.model.security_agent_outreach_domain_add_request_data_attributes import (
    SecurityAgentOutreachDomainAddRequestDataAttributes,
)
from datadog_api_client.v2.model.security_agent_outreach_domain_add_type import SecurityAgentOutreachDomainAddType

body = SecurityAgentOutreachDomainAddRequest(
    data=SecurityAgentOutreachDomainAddRequestData(
        attributes=SecurityAgentOutreachDomainAddRequestDataAttributes(
            domain="acme.com",
        ),
        type=SecurityAgentOutreachDomainAddType.OUTREACH_POLICY_DOMAIN_ADD,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["add_security_agent_outreach_policy_domain"] = True
with ApiClient(configuration) as api_client:
    api_instance = BitsSecurityAnalystApi(api_client)
    response = api_instance.add_security_agent_outreach_policy_domain(body=body)

    print(response)
