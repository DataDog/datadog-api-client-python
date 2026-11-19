"""
Create a Bits Security Analyst investigation returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.bits_security_analyst_api import BitsSecurityAnalystApi
from datadog_api_client.v2.model.security_agent_investigation_create_attributes import (
    SecurityAgentInvestigationCreateAttributes,
)
from datadog_api_client.v2.model.security_agent_investigation_create_data import SecurityAgentInvestigationCreateData
from datadog_api_client.v2.model.security_agent_investigation_create_request import (
    SecurityAgentInvestigationCreateRequest,
)
from datadog_api_client.v2.model.security_agent_investigation_type import SecurityAgentInvestigationType

body = SecurityAgentInvestigationCreateRequest(
    data=SecurityAgentInvestigationCreateData(
        attributes=SecurityAgentInvestigationCreateAttributes(
            rerun=False,
            signal_id="AQAAAaGNHjq4XzqcIQAAAABBWm8xY0wybUFBQmNYSjl1QUFBQUFBQUE",
        ),
        type=SecurityAgentInvestigationType.INVESTIGATIONS,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_security_agent_investigation"] = True
with ApiClient(configuration) as api_client:
    api_instance = BitsSecurityAnalystApi(api_client)
    response = api_instance.create_security_agent_investigation(body=body)

    print(response)
