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
    from datadog_api_client.v2.model.user_authorized_client_relationship_o_auth2_client_data_type import (
        UserAuthorizedClientRelationshipOAuth2ClientDataType,
    )


class UserAuthorizedClientRelationshipOAuth2ClientData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.user_authorized_client_relationship_o_auth2_client_data_type import (
            UserAuthorizedClientRelationshipOAuth2ClientDataType,
        )

        return {
            "id": (str,),
            "type": (UserAuthorizedClientRelationshipOAuth2ClientDataType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: UserAuthorizedClientRelationshipOAuth2ClientDataType, **kwargs):
        """
        Data identifying the OAuth2 client that was authorized.

        :param id: The ID of the OAuth2 client.
        :type id: str

        :param type: OAuth2 client resource type.
        :type type: UserAuthorizedClientRelationshipOAuth2ClientDataType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
