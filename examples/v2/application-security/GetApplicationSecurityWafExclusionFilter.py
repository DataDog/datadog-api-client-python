"""
Get a WAF exclusion filter returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.application_security_api import ApplicationSecurityApi

# there is a valid "exclusion_filter" in the system
EXCLUSION_FILTER_DATA_ID = environ["EXCLUSION_FILTER_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ApplicationSecurityApi(api_client)
    response = api_instance.get_application_security_waf_exclusion_filter(
        exclusion_filter_id=EXCLUSION_FILTER_DATA_ID,
    )

    print(response)
