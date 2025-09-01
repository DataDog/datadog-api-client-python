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
    from datadog_api_client.v2.model.issue_case_attributes import IssueCaseAttributes
    from datadog_api_client.v2.model.issue_case_relationships import IssueCaseRelationships
    from datadog_api_client.v2.model.issue_case_resource_type import IssueCaseResourceType


class IssueCase(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_case_attributes import IssueCaseAttributes
        from datadog_api_client.v2.model.issue_case_relationships import IssueCaseRelationships
        from datadog_api_client.v2.model.issue_case_resource_type import IssueCaseResourceType

        return {
            "attributes": (IssueCaseAttributes,),
            "id": (str,),
            "relationships": (IssueCaseRelationships,),
            "type": (IssueCaseResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IssueCaseAttributes,
        id: str,
        type: IssueCaseResourceType,
        relationships: Union[IssueCaseRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        The case attached to the issue.

        :param attributes: Object containing the information of a case.
        :type attributes: IssueCaseAttributes

        :param id: Case identifier.
        :type id: str

        :param relationships: Resources related to a case.
        :type relationships: IssueCaseRelationships, optional

        :param type: Type of the object.
        :type type: IssueCaseResourceType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
