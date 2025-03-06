"""
Get a WAF custom rule returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.application_security_api import ApplicationSecurityApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ApplicationSecurityApi(api_client)
    response = api_instance.get_application_security_waf_custom_rule(
        custom_rule_id="custom_rule_id",
    )

    print(response)
