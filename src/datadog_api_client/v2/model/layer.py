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
    from datadog_api_client.v2.model.layer_attributes import LayerAttributes
    from datadog_api_client.v2.model.layer_relationships import LayerRelationships
    from datadog_api_client.v2.model.layer_type import LayerType


class Layer(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.layer_attributes import LayerAttributes
        from datadog_api_client.v2.model.layer_relationships import LayerRelationships
        from datadog_api_client.v2.model.layer_type import LayerType

        return {
            "attributes": (LayerAttributes,),
            "id": (str,),
            "relationships": (LayerRelationships,),
            "type": (LayerType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        type: LayerType,
        attributes: Union[LayerAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[LayerRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Encapsulates a layer resource, holding attributes like rotation details, plus relationships to the members covering that layer.

        :param attributes: Describes key properties of a Layer, including rotation details, name, start/end times, and any restrictions.
        :type attributes: LayerAttributes, optional

        :param id: A unique identifier for this layer.
        :type id: str, optional

        :param relationships: Holds references to objects related to the Layer entity, such as its members.
        :type relationships: LayerRelationships, optional

        :param type: Layers resource type.
        :type type: LayerType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
