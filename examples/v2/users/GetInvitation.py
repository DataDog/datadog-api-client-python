"""
Get a user invitation returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.users_api import UsersApi

# the "user" has a "user_invitation"
USER_INVITATION_ID = environ["USER_INVITATION_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    response = api_instance.get_invitation(
        user_invitation_uuid=USER_INVITATION_ID,
    )

    print(response)
