"""
Get all CSM Threats Agent rules returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_threats_api import CSMThreatsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMThreatsApi(api_client)
    response = api_instance.list_csm_threats_agent_rules()

    print(response)
