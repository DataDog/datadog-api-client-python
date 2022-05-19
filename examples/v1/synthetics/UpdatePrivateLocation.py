"""
Edit a private location returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi
from datadog_api_client.v1.model.synthetics_private_location import SyntheticsPrivateLocation
from datadog_api_client.v1.model.synthetics_private_location_metadata import SyntheticsPrivateLocationMetadata
from datadog_api_client.v1.model.synthetics_restricted_roles import SyntheticsRestrictedRoles

body = SyntheticsPrivateLocation(
    description="Description of private location",
    metadata=SyntheticsPrivateLocationMetadata(
        restricted_roles=SyntheticsRestrictedRoles(
            [
                "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            ]
        ),
    ),
    name="New private location",
    tags=[
        "team:front",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.update_private_location(location_id="location_id", body=body)

    print(response)
