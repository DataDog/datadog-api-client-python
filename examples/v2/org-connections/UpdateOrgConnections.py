"""
Update Org Connection returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.org_connections_api import OrgConnectionsApi
from datadog_api_client.v2.model.org_connection_type import OrgConnectionType
from datadog_api_client.v2.model.org_connection_type_enum import OrgConnectionTypeEnum
from datadog_api_client.v2.model.org_connection_update import OrgConnectionUpdate
from datadog_api_client.v2.model.org_connection_update_attributes import OrgConnectionUpdateAttributes
from datadog_api_client.v2.model.org_connection_update_request import OrgConnectionUpdateRequest

# there is a valid "org_connection" in the system
ORG_CONNECTION_DATA_ID = environ["ORG_CONNECTION_DATA_ID"]

body = OrgConnectionUpdateRequest(
    data=OrgConnectionUpdate(
        type=OrgConnectionType.ORG_CONNECTION,
        id=ORG_CONNECTION_DATA_ID,
        attributes=OrgConnectionUpdateAttributes(
            connection_types=[
                OrgConnectionTypeEnum.LOGS,
                OrgConnectionTypeEnum.METRICS,
            ],
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OrgConnectionsApi(api_client)
    response = api_instance.update_org_connections(connection_id=ORG_CONNECTION_DATA_ID, body=body)

    print(response)
