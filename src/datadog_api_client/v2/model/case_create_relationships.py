# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.nullable_user_relationship import NullableUserRelationship
    from datadog_api_client.v2.model.project_relationship import ProjectRelationship


class CaseCreateRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.nullable_user_relationship import NullableUserRelationship
        from datadog_api_client.v2.model.project_relationship import ProjectRelationship

        return {
            "assignee": (NullableUserRelationship,),
            "project": (ProjectRelationship,),
        }

    attribute_map = {
        "assignee": "assignee",
        "project": "project",
    }

    def __init__(
        self_,
        project: ProjectRelationship,
        assignee: Union[NullableUserRelationship, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Relationships formed with the case on creation

        :param assignee: Relationship to user.
        :type assignee: NullableUserRelationship, none_type, optional

        :param project: Relationship to project
        :type project: ProjectRelationship
        """
        if assignee is not unset:
            kwargs["assignee"] = assignee
        super().__init__(kwargs)

        self_.project = project
