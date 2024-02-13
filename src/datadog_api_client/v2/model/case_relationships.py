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


class CaseRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.nullable_user_relationship import NullableUserRelationship
        from datadog_api_client.v2.model.project_relationship import ProjectRelationship

        return {
            "assignee": (NullableUserRelationship,),
            "created_by": (NullableUserRelationship,),
            "modified_by": (NullableUserRelationship,),
            "project": (ProjectRelationship,),
        }

    attribute_map = {
        "assignee": "assignee",
        "created_by": "created_by",
        "modified_by": "modified_by",
        "project": "project",
    }

    def __init__(
        self_,
        assignee: Union[NullableUserRelationship, none_type, UnsetType] = unset,
        created_by: Union[NullableUserRelationship, none_type, UnsetType] = unset,
        modified_by: Union[NullableUserRelationship, none_type, UnsetType] = unset,
        project: Union[ProjectRelationship, UnsetType] = unset,
        **kwargs,
    ):
        """
        Resources related to a case

        :param assignee: Relationship to user.
        :type assignee: NullableUserRelationship, none_type, optional

        :param created_by: Relationship to user.
        :type created_by: NullableUserRelationship, none_type, optional

        :param modified_by: Relationship to user.
        :type modified_by: NullableUserRelationship, none_type, optional

        :param project: Relationship to project
        :type project: ProjectRelationship, optional
        """
        if assignee is not unset:
            kwargs["assignee"] = assignee
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if modified_by is not unset:
            kwargs["modified_by"] = modified_by
        if project is not unset:
            kwargs["project"] = project
        super().__init__(kwargs)
