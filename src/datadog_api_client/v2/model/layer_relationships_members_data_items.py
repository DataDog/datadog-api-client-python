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
    from datadog_api_client.v2.model.layer_relationships_members_data_items_type import (
        LayerRelationshipsMembersDataItemsType,
    )


class LayerRelationshipsMembersDataItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.layer_relationships_members_data_items_type import (
            LayerRelationshipsMembersDataItemsType,
        )

        return {
            "id": (str,),
            "type": (LayerRelationshipsMembersDataItemsType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: Union[str, UnsetType] = unset,
        type: Union[LayerRelationshipsMembersDataItemsType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Represents a single member object in a layer's ``members`` array, referencing
        a unique Datadog user ID.

        :param id: The unique user ID of the layer member.
        :type id: str, optional

        :param type: Members resource type.
        :type type: LayerRelationshipsMembersDataItemsType, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
