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
    from datadog_api_client.v2.model.issue_attributes import IssueAttributes
    from datadog_api_client.v2.model.issue_relationships import IssueRelationships
    from datadog_api_client.v2.model.issue_type import IssueType


class Issue(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_attributes import IssueAttributes
        from datadog_api_client.v2.model.issue_relationships import IssueRelationships
        from datadog_api_client.v2.model.issue_type import IssueType

        return {
            "attributes": (IssueAttributes,),
            "id": (str,),
            "relationships": (IssueRelationships,),
            "type": (IssueType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IssueAttributes,
        id: str,
        type: IssueType,
        relationships: Union[IssueRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        The issue matching the request.

        :param attributes: Object containing the information of an issue.
        :type attributes: IssueAttributes

        :param id: Issue identifier.
        :type id: str

        :param relationships: Relationship between the issue and an assignee, case and/or teams.
        :type relationships: IssueRelationships, optional

        :param type: Type of the object.
        :type type: IssueType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
