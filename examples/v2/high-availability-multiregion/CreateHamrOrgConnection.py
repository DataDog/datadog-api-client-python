"""
Create or update HAMR organization connection returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.high_availability_multi_region_api import HighAvailabilityMultiRegionApi
from datadog_api_client.v2.model.hamr_org_connection_attributes_request import HamrOrgConnectionAttributesRequest
from datadog_api_client.v2.model.hamr_org_connection_data_request import HamrOrgConnectionDataRequest
from datadog_api_client.v2.model.hamr_org_connection_request import HamrOrgConnectionRequest
from datadog_api_client.v2.model.hamr_org_connection_status import HamrOrgConnectionStatus
from datadog_api_client.v2.model.hamr_org_connection_type import HamrOrgConnectionType

body = HamrOrgConnectionRequest(
    data=HamrOrgConnectionDataRequest(
        attributes=HamrOrgConnectionAttributesRequest(
            hamr_status=HamrOrgConnectionStatus.ACTIVE,
            is_primary=True,
            modified_by="admin@example.com",
            target_org_datacenter="us1",
            target_org_name="Production Backup Org",
            target_org_uuid="660f9511-f3ac-52e5-b827-557766551111",
        ),
        id="550e8400-e29b-41d4-a716-446655440000",
        type=HamrOrgConnectionType.HAMR_ORG_CONNECTIONS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_hamr_org_connection"] = True
with ApiClient(configuration) as api_client:
    api_instance = HighAvailabilityMultiRegionApi(api_client)
    response = api_instance.create_hamr_org_connection(body=body)

    print(response)
