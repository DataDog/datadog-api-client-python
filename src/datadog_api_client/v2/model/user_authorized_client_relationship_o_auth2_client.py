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
    from datadog_api_client.v2.model.user_authorized_client_relationship_o_auth2_client_data import (
        UserAuthorizedClientRelationshipOAuth2ClientData,
    )


class UserAuthorizedClientRelationshipOAuth2Client(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.user_authorized_client_relationship_o_auth2_client_data import (
            UserAuthorizedClientRelationshipOAuth2ClientData,
        )

        return {
            "data": (UserAuthorizedClientRelationshipOAuth2ClientData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: UserAuthorizedClientRelationshipOAuth2ClientData, **kwargs):
        """
        Relationship to the OAuth2 client that was authorized.

        :param data: Data identifying the OAuth2 client that was authorized.
        :type data: UserAuthorizedClientRelationshipOAuth2ClientData
        """
        super().__init__(kwargs)

        self_.data = data
