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
    from datadog_api_client.v2.model.user_authorized_client_relationship_user_data_type import (
        UserAuthorizedClientRelationshipUserDataType,
    )


class UserAuthorizedClientRelationshipUserData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.user_authorized_client_relationship_user_data_type import (
            UserAuthorizedClientRelationshipUserDataType,
        )

        return {
            "id": (str,),
            "type": (UserAuthorizedClientRelationshipUserDataType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: UserAuthorizedClientRelationshipUserDataType, **kwargs):
        """
        Data identifying the user who granted this authorization.

        :param id: The ID of the user.
        :type id: str

        :param type: User resource type.
        :type type: UserAuthorizedClientRelationshipUserDataType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
