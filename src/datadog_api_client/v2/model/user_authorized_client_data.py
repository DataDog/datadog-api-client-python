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
    from datadog_api_client.v2.model.user_authorized_client_attributes import UserAuthorizedClientAttributes
    from datadog_api_client.v2.model.user_authorized_client_relationships import UserAuthorizedClientRelationships
    from datadog_api_client.v2.model.user_authorized_client_type import UserAuthorizedClientType


class UserAuthorizedClientData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.user_authorized_client_attributes import UserAuthorizedClientAttributes
        from datadog_api_client.v2.model.user_authorized_client_relationships import UserAuthorizedClientRelationships
        from datadog_api_client.v2.model.user_authorized_client_type import UserAuthorizedClientType

        return {
            "attributes": (UserAuthorizedClientAttributes,),
            "id": (str,),
            "relationships": (UserAuthorizedClientRelationships,),
            "type": (UserAuthorizedClientType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: UserAuthorizedClientAttributes,
        id: str,
        relationships: UserAuthorizedClientRelationships,
        type: UserAuthorizedClientType,
        **kwargs,
    ):
        """
        Data object representing a user authorized client.

        :param attributes: Attributes of a user authorized client.
        :type attributes: UserAuthorizedClientAttributes

        :param id: The unique identifier of the user authorized client.
        :type id: str

        :param relationships: Relationships for a user authorized client.
        :type relationships: UserAuthorizedClientRelationships

        :param type: The resource type for user authorized clients.
        :type type: UserAuthorizedClientType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.relationships = relationships
        self_.type = type
