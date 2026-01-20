"""
Get all suppression rules returns "OK" response with pagination
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

# there is a valid "suppression" in the system
SUPPRESSION_DATA_ID = environ["SUPPRESSION_DATA_ID"]

# there is a valid "suppression2" in the system
SUPPRESSION2_DATA_ID = environ["SUPPRESSION2_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.list_security_monitoring_suppressions(
        query="id:3dd-0uc-h1s OR id:886e6c3e-e543-049c-ee1b-56a1110295c0",
        page_size=1,
        page_number=0,
    )

    print(response)
