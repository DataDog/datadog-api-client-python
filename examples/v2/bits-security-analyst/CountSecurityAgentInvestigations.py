"""
Count Bits Security Analyst investigations returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.bits_security_analyst_api import BitsSecurityAnalystApi
from datadog_api_client.v2.model.security_agent_investigation_count_field import SecurityAgentInvestigationCountField

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["count_security_agent_investigations"] = True
with ApiClient(configuration) as api_client:
    api_instance = BitsSecurityAnalystApi(api_client)
    response = api_instance.count_security_agent_investigations(
        field=SecurityAgentInvestigationCountField.VERDICT,
    )

    print(response)
