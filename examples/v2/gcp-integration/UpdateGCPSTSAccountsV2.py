"""
Update STS Service Account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.gcp_integration_api import GCPIntegrationApi
from datadog_api_client.v2.model.account_attributes import AccountAttributes
from datadog_api_client.v2.model.account_patch_body import AccountPatchBody
from datadog_api_client.v2.model.service_account_info_patch import ServiceAccountInfoPatch

body = AccountPatchBody(
    data=ServiceAccountInfoPatch(
        attributes=AccountAttributes(
            client_email="datadog-service-account@test-project.iam.gserviceaccount.com",
            host_filters=[],
        ),
        id="d291291f-12c2-22g4-j290-123456678897",
        type="gcp_service_account",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GCPIntegrationApi(api_client)
    response = api_instance.update_gcpsts_accounts_v2(account_id="account_id", body=body)

    print(response)
