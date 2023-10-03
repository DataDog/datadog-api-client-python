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
    from datadog_api_client.v2.model.powerpack_attributes import PowerpackAttributes
    from datadog_api_client.v2.model.powerpack_relationships import PowerpackRelationships


class PowerpackData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.powerpack_attributes import PowerpackAttributes
        from datadog_api_client.v2.model.powerpack_relationships import PowerpackRelationships

        return {
            "attributes": (PowerpackAttributes,),
            "id": (str,),
            "relationships": (PowerpackRelationships,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[PowerpackAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[PowerpackRelationships, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Powerpack data object.

        :param attributes: Powerpack attribute object.
        :type attributes: PowerpackAttributes, optional

        :param id: ID of the powerpack.
        :type id: str, optional

        :param relationships: Powerpack relationship object.
        :type relationships: PowerpackRelationships, optional

        :param type: Type of widget, must be powerpack.
        :type type: str, optional
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
