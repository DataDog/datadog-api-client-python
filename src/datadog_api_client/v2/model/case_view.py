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
    from datadog_api_client.v2.model.case_view_attributes import CaseViewAttributes
    from datadog_api_client.v2.model.case_view_relationships import CaseViewRelationships
    from datadog_api_client.v2.model.case_view_resource_type import CaseViewResourceType


class CaseView(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_view_attributes import CaseViewAttributes
        from datadog_api_client.v2.model.case_view_relationships import CaseViewRelationships
        from datadog_api_client.v2.model.case_view_resource_type import CaseViewResourceType

        return {
            "attributes": (CaseViewAttributes,),
            "id": (str,),
            "relationships": (CaseViewRelationships,),
            "type": (CaseViewResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: CaseViewAttributes,
        id: str,
        type: CaseViewResourceType,
        relationships: Union[CaseViewRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        A saved case view that provides a filtered, reusable list of cases matching a specific query. Views act as persistent dashboards for monitoring case subsets.

        :param attributes: Attributes of a case view, including the filter query and optional notification rule.
        :type attributes: CaseViewAttributes

        :param id: The view's identifier.
        :type id: str

        :param relationships: Related resources for the case view, including the creator, last modifier, and associated project.
        :type relationships: CaseViewRelationships, optional

        :param type: JSON:API resource type for case views.
        :type type: CaseViewResourceType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
