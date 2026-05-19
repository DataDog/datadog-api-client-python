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
    from datadog_api_client.v2.model.case_create_attributes import CaseCreateAttributes
    from datadog_api_client.v2.model.case_create_relationships import CaseCreateRelationships
    from datadog_api_client.v2.model.case_resource_type import CaseResourceType


class CaseCreate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_create_attributes import CaseCreateAttributes
        from datadog_api_client.v2.model.case_create_relationships import CaseCreateRelationships
        from datadog_api_client.v2.model.case_resource_type import CaseResourceType

        return {
            "attributes": (CaseCreateAttributes,),
            "relationships": (CaseCreateRelationships,),
            "type": (CaseResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: CaseCreateAttributes,
        type: CaseResourceType,
        relationships: Union[CaseCreateRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Case creation data

        :param attributes: Case creation attributes
        :type attributes: CaseCreateAttributes

        :param relationships: Relationships formed with the case on creation
        :type relationships: CaseCreateRelationships, optional

        :param type: Case resource type
        :type type: CaseResourceType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
