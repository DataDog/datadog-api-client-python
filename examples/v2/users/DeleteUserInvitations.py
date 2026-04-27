"""
Delete a pending user's invitations returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.users_api import UsersApi
from uuid import UUID

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    api_instance.delete_user_invitations(
        user_id=UUID("4dee724d-00cc-11ea-a77b-570c9d03c6c5"),
    )
