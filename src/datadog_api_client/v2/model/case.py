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
    from datadog_api_client.v2.model.case_attributes import CaseAttributes
    from datadog_api_client.v2.model.case_relationships import CaseRelationships
    from datadog_api_client.v2.model.case_resource_type import CaseResourceType


class Case(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_attributes import CaseAttributes
        from datadog_api_client.v2.model.case_relationships import CaseRelationships
        from datadog_api_client.v2.model.case_resource_type import CaseResourceType

        return {
            "attributes": (CaseAttributes,),
            "id": (str,),
            "relationships": (CaseRelationships,),
            "type": (CaseResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: CaseAttributes,
        id: str,
        type: CaseResourceType,
        relationships: Union[CaseRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        A case

        :param attributes: Case attributes
        :type attributes: CaseAttributes

        :param id: Case's identifier
        :type id: str

        :param relationships: Resources related to a case
        :type relationships: CaseRelationships, optional

        :param type: Case resource type
        :type type: CaseResourceType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
