"""
Update an org authorized client returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.org_authorized_clients_api import OrgAuthorizedClientsApi
from datadog_api_client.v2.model.org_authorized_client_type import OrgAuthorizedClientType
from datadog_api_client.v2.model.org_authorized_client_update_attributes import OrgAuthorizedClientUpdateAttributes
from datadog_api_client.v2.model.org_authorized_client_update_data import OrgAuthorizedClientUpdateData
from datadog_api_client.v2.model.org_authorized_client_update_request import OrgAuthorizedClientUpdateRequest

body = OrgAuthorizedClientUpdateRequest(
    data=OrgAuthorizedClientUpdateData(
        attributes=OrgAuthorizedClientUpdateAttributes(
            disabled=True,
        ),
        id="00000000-0000-0000-0000-000000000001",
        type=OrgAuthorizedClientType.ORG_AUTHORIZED_CLIENTS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OrgAuthorizedClientsApi(api_client)
    response = api_instance.update_org_authorized_client(
        org_authorized_client_id="00000000-0000-0000-0000-000000000001", body=body
    )

    print(response)
