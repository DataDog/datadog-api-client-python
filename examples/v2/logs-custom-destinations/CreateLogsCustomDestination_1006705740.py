"""
Create a Google Security Operations custom destination returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_custom_destinations_api import LogsCustomDestinationsApi
from datadog_api_client.v2.model.custom_destination_attribute_tags_restriction_list_type import (
    CustomDestinationAttributeTagsRestrictionListType,
)
from datadog_api_client.v2.model.custom_destination_create_request import CustomDestinationCreateRequest
from datadog_api_client.v2.model.custom_destination_create_request_attributes import (
    CustomDestinationCreateRequestAttributes,
)
from datadog_api_client.v2.model.custom_destination_create_request_definition import (
    CustomDestinationCreateRequestDefinition,
)
from datadog_api_client.v2.model.custom_destination_forward_destination_google_security_operations import (
    CustomDestinationForwardDestinationGoogleSecurityOperations,
)
from datadog_api_client.v2.model.custom_destination_forward_destination_google_security_operations_type import (
    CustomDestinationForwardDestinationGoogleSecurityOperationsType,
)
from datadog_api_client.v2.model.custom_destination_google_security_operations_destination_auth import (
    CustomDestinationGoogleSecurityOperationsDestinationAuth,
)
from datadog_api_client.v2.model.custom_destination_google_security_operations_destination_auth_type import (
    CustomDestinationGoogleSecurityOperationsDestinationAuthType,
)
from datadog_api_client.v2.model.custom_destination_type import CustomDestinationType

body = CustomDestinationCreateRequest(
    data=CustomDestinationCreateRequestDefinition(
        attributes=CustomDestinationCreateRequestAttributes(
            enabled=False,
            forward_tags=False,
            forward_tags_restriction_list=[
                "datacenter",
                "host",
            ],
            forward_tags_restriction_list_type=CustomDestinationAttributeTagsRestrictionListType.ALLOW_LIST,
            forwarder_destination=CustomDestinationForwardDestinationGoogleSecurityOperations(
                type=CustomDestinationForwardDestinationGoogleSecurityOperationsType.GOOGLE_SECURITY_OPERATIONS,
                customer_id="123-456-7890",
                regional_endpoint="https://malachiteingestion-pa.googleapis.com",
                namespace="google-security-operations-namespace",
                auth=CustomDestinationGoogleSecurityOperationsDestinationAuth(
                    type=CustomDestinationGoogleSecurityOperationsDestinationAuthType.GCP_PRIVATE_KEY,
                    project_id="gcp-project",
                    private_key_id="abc12345678",
                    client_email="client@example.com",
                    client_id="def123456",
                    private_key="-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBK...\n-----END PRIVATE KEY-----\n",
                ),
            ),
            name="Nginx logs",
            query="source:nginx",
        ),
        type=CustomDestinationType.CUSTOM_DESTINATION,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsCustomDestinationsApi(api_client)
    response = api_instance.create_logs_custom_destination(body=body)

    print(response)
