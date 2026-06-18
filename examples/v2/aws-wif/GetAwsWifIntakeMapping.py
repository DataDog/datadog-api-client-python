"""
Get an AWS WIF intake mapping returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.awswif_api import AWSWIFApi
from uuid import UUID

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSWIFApi(api_client)
    response = api_instance.get_aws_wif_intake_mapping(
        config_uuid=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
    )

    print(response)
