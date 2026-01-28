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
    from datadog_api_client.v2.model.user_relationship_data import UserRelationshipData


class ProjectFavoriteUserRelationship(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.user_relationship_data import UserRelationshipData

        return {
            "data": (UserRelationshipData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: UserRelationshipData, **kwargs):
        """
        Relationship to user

        :param data: Relationship to user object.
        :type data: UserRelationshipData
        """
        super().__init__(kwargs)

        self_.data = data
