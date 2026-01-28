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
    from datadog_api_client.v2.model.project_favorite_user_relationship import ProjectFavoriteUserRelationship


class ProjectFavoriteRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.project_favorite_user_relationship import ProjectFavoriteUserRelationship

        return {
            "user": (ProjectFavoriteUserRelationship,),
        }

    attribute_map = {
        "user": "user",
    }

    def __init__(self_, user: ProjectFavoriteUserRelationship, **kwargs):
        """
        Project favorite relationships

        :param user: Relationship to user
        :type user: ProjectFavoriteUserRelationship
        """
        super().__init__(kwargs)

        self_.user = user
