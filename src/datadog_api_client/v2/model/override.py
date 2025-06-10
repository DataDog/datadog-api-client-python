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
    from datadog_api_client.v2.model.override_type import OverrideType


class Override(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.override_attributes import OverrideAttributes
        from datadog_api_client.v2.model.override_relationships import OverrideRelationships
        from datadog_api_client.v2.model.override_type import OverrideType

        return {
            "attributes": (OverrideAttributes,),
            "id": (str,),
            "relationships": (OverrideRelationships,),
            "type": (OverrideType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[OverrideAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[OverrideRelationships, UnsetType] = unset,
        type: Union[OverrideType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``Override`` object.

        :param attributes: The definition of ``OverrideAttributes`` object.
        :type attributes: OverrideAttributes, optional

        :param id: The ID of the override.
        :type id: str, optional

        :param relationships: The definition of ``OverrideRelationships`` object.
        :type relationships: OverrideRelationships, optional

        :param type: The definition of ``OverrideType`` object.
        :type type: OverrideType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
