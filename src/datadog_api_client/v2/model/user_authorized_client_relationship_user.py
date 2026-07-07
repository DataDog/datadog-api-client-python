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
    from datadog_api_client.v2.model.user_authorized_client_relationship_user_data import (
        UserAuthorizedClientRelationshipUserData,
    )


class UserAuthorizedClientRelationshipUser(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.user_authorized_client_relationship_user_data import (
            UserAuthorizedClientRelationshipUserData,
        )

        return {
            "data": (UserAuthorizedClientRelationshipUserData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: UserAuthorizedClientRelationshipUserData, **kwargs):
        """
        Relationship to the user who granted this authorization.

        :param data: Data identifying the user who granted this authorization.
        :type data: UserAuthorizedClientRelationshipUserData
        """
        super().__init__(kwargs)

        self_.data = data
