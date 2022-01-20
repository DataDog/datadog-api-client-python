"""
Get all security filters returns "OK" response
"""

from datadog_api_client.v2 import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_siem_api import CloudSIEMApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudSIEMApi(api_client)
    response = api_instance.list_security_filters()

    print(response)
