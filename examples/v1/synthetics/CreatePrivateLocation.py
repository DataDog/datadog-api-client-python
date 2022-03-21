"""
Create a private location returns "OK" response
"""

from datadog_api_client.v1 import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi
from datadog_api_client.v1.model.synthetics_private_location import SyntheticsPrivateLocation

body = SyntheticsPrivateLocation(
    description="Description of private location", name="New private location", tags=["team:front"]
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.create_private_location(body=body)

    print(response)
