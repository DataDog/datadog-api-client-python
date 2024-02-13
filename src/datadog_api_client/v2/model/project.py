# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.project_attributes import ProjectAttributes
    from datadog_api_client.v2.model.project_relationships import ProjectRelationships
    from datadog_api_client.v2.model.project_resource_type import ProjectResourceType


class Project(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.project_attributes import ProjectAttributes
        from datadog_api_client.v2.model.project_relationships import ProjectRelationships
        from datadog_api_client.v2.model.project_resource_type import ProjectResourceType

        return {
            "attributes": (ProjectAttributes,),
            "id": (str,),
            "relationships": (ProjectRelationships,),
            "type": (ProjectResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ProjectAttributes,
        id: str,
        type: ProjectResourceType,
        relationships: Union[ProjectRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        A Project

        :param attributes: Project attributes
        :type attributes: ProjectAttributes

        :param id: The Project's identifier
        :type id: str

        :param relationships: Project relationships
        :type relationships: ProjectRelationships, optional

        :param type: Project resource type
        :type type: ProjectResourceType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
