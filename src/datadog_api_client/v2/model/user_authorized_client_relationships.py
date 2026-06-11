# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.user_authorized_client_relationship_o_auth2_client import (
        UserAuthorizedClientRelationshipOAuth2Client,
    )
    from datadog_api_client.v2.model.user_authorized_client_relationship_scopes import (
        UserAuthorizedClientRelationshipScopes,
    )
    from datadog_api_client.v2.model.user_authorized_client_relationship_user import (
        UserAuthorizedClientRelationshipUser,
    )


class UserAuthorizedClientRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.user_authorized_client_relationship_o_auth2_client import (
            UserAuthorizedClientRelationshipOAuth2Client,
        )
        from datadog_api_client.v2.model.user_authorized_client_relationship_scopes import (
            UserAuthorizedClientRelationshipScopes,
        )
        from datadog_api_client.v2.model.user_authorized_client_relationship_user import (
            UserAuthorizedClientRelationshipUser,
        )

        return {
            "oauth2_client": (UserAuthorizedClientRelationshipOAuth2Client,),
            "scopes": (UserAuthorizedClientRelationshipScopes,),
            "user": (UserAuthorizedClientRelationshipUser,),
        }

    attribute_map = {
        "oauth2_client": "oauth2_client",
        "scopes": "scopes",
        "user": "user",
    }

    def __init__(
        self_,
        oauth2_client: UserAuthorizedClientRelationshipOAuth2Client,
        scopes: UserAuthorizedClientRelationshipScopes,
        user: UserAuthorizedClientRelationshipUser,
        **kwargs,
    ):
        """
        Relationships for a user authorized client.

        :param oauth2_client: Relationship to the OAuth2 client that was authorized.
        :type oauth2_client: UserAuthorizedClientRelationshipOAuth2Client

        :param scopes: Relationship to the scopes granted to the OAuth2 client.
        :type scopes: UserAuthorizedClientRelationshipScopes

        :param user: Relationship to the user who granted this authorization.
        :type user: UserAuthorizedClientRelationshipUser
        """
        super().__init__(kwargs)

        self_.oauth2_client = oauth2_client
        self_.scopes = scopes
        self_.user = user
