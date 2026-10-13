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
    from datadog_api_client.v2.model.override_attributes import OverrideAttributes
    from datadog_api_client.v2.model.override_relationships import OverrideRelationships
    from datadog_api_client.v2.model.override_data_type import OverrideDataType


class OverrideData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.override_attributes import OverrideAttributes
        from datadog_api_client.v2.model.override_relationships import OverrideRelationships
        from datadog_api_client.v2.model.override_data_type import OverrideDataType

        return {
            "attributes": (OverrideAttributes,),
            "id": (str,),
            "relationships": (OverrideRelationships,),
            "type": (OverrideDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: OverrideDataType,
        attributes: Union[OverrideAttributes, UnsetType] = unset,
        relationships: Union[OverrideRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data for an on-call schedule override.

        :param attributes: Attributes for an on-call schedule override.
        :type attributes: OverrideAttributes, optional

        :param id: The unique identifier of the override.
        :type id: str

        :param relationships: Relationships for an on-call schedule override.
        :type relationships: OverrideRelationships, optional

        :param type: Indicates that the resource is of type 'overrides'.
        :type type: OverrideDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
