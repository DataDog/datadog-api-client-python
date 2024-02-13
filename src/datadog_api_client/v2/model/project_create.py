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
    from datadog_api_client.v2.model.project_create_attributes import ProjectCreateAttributes
    from datadog_api_client.v2.model.project_resource_type import ProjectResourceType


class ProjectCreate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.project_create_attributes import ProjectCreateAttributes
        from datadog_api_client.v2.model.project_resource_type import ProjectResourceType

        return {
            "attributes": (ProjectCreateAttributes,),
            "type": (ProjectResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: ProjectCreateAttributes, type: ProjectResourceType, **kwargs):
        """
        Project create

        :param attributes: Project creation attributes
        :type attributes: ProjectCreateAttributes

        :param type: Project resource type
        :type type: ProjectResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
