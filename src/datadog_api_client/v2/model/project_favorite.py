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
    from datadog_api_client.v2.model.project_favorite_resource_type import ProjectFavoriteResourceType


class ProjectFavorite(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.project_favorite_resource_type import ProjectFavoriteResourceType

        return {
            "id": (str,),
            "type": (ProjectFavoriteResourceType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: ProjectFavoriteResourceType, **kwargs):
        """
        Represents a case project that the current user has bookmarked for quick access. Favorited projects appear prominently in the Case Management UI.

        :param id: The UUID of the favorited project.
        :type id: str

        :param type: JSON:API resource type for project favorites.
        :type type: ProjectFavoriteResourceType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
