"""
Upsert an OAuth2 client scopes restriction returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.o_auth2_client_public_api import OAuth2ClientPublicApi
from datadog_api_client.v2.model.o_auth_oidc_scope import OAuthOidcScope
from datadog_api_client.v2.model.upsert_o_auth_scopes_restriction_data import UpsertOAuthScopesRestrictionData
from datadog_api_client.v2.model.upsert_o_auth_scopes_restriction_data_attributes import (
    UpsertOAuthScopesRestrictionDataAttributes,
)
from datadog_api_client.v2.model.upsert_o_auth_scopes_restriction_request import UpsertOAuthScopesRestrictionRequest
from datadog_api_client.v2.model.upsert_o_auth_scopes_restriction_type import UpsertOAuthScopesRestrictionType
from uuid import UUID

body = UpsertOAuthScopesRestrictionRequest(
    data=UpsertOAuthScopesRestrictionData(
        attributes=UpsertOAuthScopesRestrictionDataAttributes(
            oidc_scopes=[
                OAuthOidcScope.OPENID,
                OAuthOidcScope.EMAIL,
            ],
            permission_scopes=[
                "dashboards_read",
                "metrics_read",
            ],
        ),
        type=UpsertOAuthScopesRestrictionType.UPSERT_SCOPES_RESTRICTION,
    ),
)

configuration = Configuration()
configuration.unstable_operations["upsert_scopes_restriction"] = True
with ApiClient(configuration) as api_client:
    api_instance = OAuth2ClientPublicApi(api_client)
    response = api_instance.upsert_scopes_restriction(
        client_uuid=UUID("fafa8e1c-36a5-11f0-a83d-da7ad0900001"), body=body
    )

    print(response)
