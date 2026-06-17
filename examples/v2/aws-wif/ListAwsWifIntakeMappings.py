"""
List AWS WIF intake mappings returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.awswif_api import AWSWIFApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSWIFApi(api_client)
    response = api_instance.list_aws_wif_intake_mappings()

    print(response)
