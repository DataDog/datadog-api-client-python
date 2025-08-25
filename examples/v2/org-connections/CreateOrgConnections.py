"""
Create Org Connection returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.org_connections_api import OrgConnectionsApi
from datadog_api_client.v2.model.org_connection_create import OrgConnectionCreate
from datadog_api_client.v2.model.org_connection_create_attributes import OrgConnectionCreateAttributes
from datadog_api_client.v2.model.org_connection_create_relationships import OrgConnectionCreateRelationships
from datadog_api_client.v2.model.org_connection_create_request import OrgConnectionCreateRequest
from datadog_api_client.v2.model.org_connection_org_relationship import OrgConnectionOrgRelationship
from datadog_api_client.v2.model.org_connection_org_relationship_data import OrgConnectionOrgRelationshipData
from datadog_api_client.v2.model.org_connection_org_relationship_data_type import OrgConnectionOrgRelationshipDataType
from datadog_api_client.v2.model.org_connection_type import OrgConnectionType
from datadog_api_client.v2.model.org_connection_type_enum import OrgConnectionTypeEnum

body = OrgConnectionCreateRequest(
    data=OrgConnectionCreate(
        type=OrgConnectionType.ORG_CONNECTION,
        relationships=OrgConnectionCreateRelationships(
            sink_org=OrgConnectionOrgRelationship(
                data=OrgConnectionOrgRelationshipData(
                    type=OrgConnectionOrgRelationshipDataType.ORGS,
                    id="83999dcd-7f97-11f0-8de1-1ecf66f1aa85",
                ),
            ),
        ),
        attributes=OrgConnectionCreateAttributes(
            connection_types=[
                OrgConnectionTypeEnum.LOGS,
            ],
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OrgConnectionsApi(api_client)
    response = api_instance.create_org_connections(body=body)

    print(response)
