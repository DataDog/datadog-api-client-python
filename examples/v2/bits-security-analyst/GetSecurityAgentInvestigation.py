"""
Get a Bits Security Analyst investigation returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.bits_security_analyst_api import BitsSecurityAnalystApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["get_security_agent_investigation"] = True
with ApiClient(configuration) as api_client:
    api_instance = BitsSecurityAnalystApi(api_client)
    response = api_instance.get_security_agent_investigation(
        investigation_id="investigation_id",
    )

    print(response)
