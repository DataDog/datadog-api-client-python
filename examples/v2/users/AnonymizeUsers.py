"""
Anonymize users returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.users_api import UsersApi
from datadog_api_client.v2.model.anonymize_users_request import AnonymizeUsersRequest
from datadog_api_client.v2.model.anonymize_users_request_attributes import AnonymizeUsersRequestAttributes
from datadog_api_client.v2.model.anonymize_users_request_data import AnonymizeUsersRequestData
from datadog_api_client.v2.model.anonymize_users_request_type import AnonymizeUsersRequestType

body = AnonymizeUsersRequest(
    data=AnonymizeUsersRequestData(
        attributes=AnonymizeUsersRequestAttributes(
            user_ids=[
                "00000000-0000-0000-0000-000000000000",
            ],
        ),
        id="00000000-0000-0000-0000-000000000000",
        type=AnonymizeUsersRequestType.ANONYMIZE_USERS_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["anonymize_users"] = True
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    response = api_instance.anonymize_users(body=body)

    print(response)
