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
    from datadog_api_client.v2.model.project_favorite_relationships import ProjectFavoriteRelationships
    from datadog_api_client.v2.model.project_favorite_resource_type import ProjectFavoriteResourceType


class ProjectFavorite(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.project_favorite_relationships import ProjectFavoriteRelationships
        from datadog_api_client.v2.model.project_favorite_resource_type import ProjectFavoriteResourceType

        return {
            "id": (str,),
            "relationships": (ProjectFavoriteRelationships,),
            "type": (ProjectFavoriteResourceType,),
        }

    attribute_map = {
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_, id: str, relationships: ProjectFavoriteRelationships, type: ProjectFavoriteResourceType, **kwargs
    ):
        """
        Project favorite

        :param id: The project's identifier
        :type id: str

        :param relationships: Project favorite relationships
        :type relationships: ProjectFavoriteRelationships

        :param type: Project favorite resource type
        :type type: ProjectFavoriteResourceType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.relationships = relationships
        self_.type = type
