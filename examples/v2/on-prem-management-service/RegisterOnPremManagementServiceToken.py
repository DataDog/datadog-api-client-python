"""
Register a token returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_prem_management_service_api import OnPremManagementServiceApi
from datadog_api_client.v2.model.on_prem_management_service_register_token_attributes import (
    OnPremManagementServiceRegisterTokenAttributes,
)
from datadog_api_client.v2.model.on_prem_management_service_register_token_data_request import (
    OnPremManagementServiceRegisterTokenDataRequest,
)
from datadog_api_client.v2.model.on_prem_management_service_register_token_request import (
    OnPremManagementServiceRegisterTokenRequest,
)
from datadog_api_client.v2.model.on_prem_management_service_register_token_type import (
    OnPremManagementServiceRegisterTokenType,
)
from uuid import UUID

body = OnPremManagementServiceRegisterTokenRequest(
    data=OnPremManagementServiceRegisterTokenDataRequest(
        attributes=OnPremManagementServiceRegisterTokenAttributes(
            app_id=UUID("9a93d314-ca37-461d-b18e-0587f03c6e2a"),
            app_version=5,
            connection_id=UUID("2f66ec56-d1f3-4a18-908d-5e8c12dfb3b0"),
            query_id=UUID("8744d459-18aa-405b-821e-df9bb101c01e"),
            runner_id="runner-GBUyh2Tm6oKS6ap4kt8Bbx",
        ),
        type=OnPremManagementServiceRegisterTokenType.REGISTERTOKENREQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["register_on_prem_management_service_token"] = True
with ApiClient(configuration) as api_client:
    api_instance = OnPremManagementServiceApi(api_client)
    response = api_instance.register_on_prem_management_service_token(body=body)

    print(response)
