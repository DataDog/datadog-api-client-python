"""
Get a WAF Policy returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.application_security_api import ApplicationSecurityApi

# there is a valid "policy" in the system
POLICY_DATA_ID = environ["POLICY_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ApplicationSecurityApi(api_client)
    response = api_instance.get_application_security_waf_policy(
        policy_id=POLICY_DATA_ID,
    )

    print(response)
