"""
Create a private location returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi
from datadog_api_client.v1.model.synthetics_private_location import SyntheticsPrivateLocation
from datadog_api_client.v1.model.synthetics_private_location_metadata import SyntheticsPrivateLocationMetadata
from datadog_api_client.v1.model.synthetics_restricted_roles import SyntheticsRestrictedRoles

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

body = SyntheticsPrivateLocation(
    description="Test Example-Create_a_private_location_returns_OK_response description",
    metadata=SyntheticsPrivateLocationMetadata(
        restricted_roles=SyntheticsRestrictedRoles(
            [
                ROLE_DATA_ID,
            ]
        ),
    ),
    name="Example-Create_a_private_location_returns_OK_response",
    tags=[
        "test:examplecreateaprivatelocationreturnsokresponse",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.create_private_location(body=body)

    print(response)
