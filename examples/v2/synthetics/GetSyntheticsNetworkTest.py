"""
Get a Network Path test returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.synthetics_api import SyntheticsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.get_synthetics_network_test(
        public_id="c7a-uwa-wn2",
    )

    print(response)
