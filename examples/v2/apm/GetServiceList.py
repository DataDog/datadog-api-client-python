"""
Get service list returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.apm_api import APMApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = APMApi(api_client)
    response = api_instance.get_service_list()

    print(response)
