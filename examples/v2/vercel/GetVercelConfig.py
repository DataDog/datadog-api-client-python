"""
Get Vercel configuration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.vercel_api import VercelApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = VercelApi(api_client)
    response = api_instance.get_vercel_config(
        configuration_id="configuration_id",
    )

    print(response)
