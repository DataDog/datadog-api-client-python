"""
Get a suppression rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

# there is a valid "suppression" in the system
SUPPRESSION_DATA_ID = environ["SUPPRESSION_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.get_security_monitoring_suppression(
        suppression_id=SUPPRESSION_DATA_ID,
    )

    print(response)
