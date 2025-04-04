# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.layer_relationships_members_data_items import LayerRelationshipsMembersDataItems


class LayerRelationshipsMembers(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.layer_relationships_members_data_items import (
            LayerRelationshipsMembersDataItems,
        )

        return {
            "data": ([LayerRelationshipsMembersDataItems],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[List[LayerRelationshipsMembersDataItems], UnsetType] = unset, **kwargs):
        """
        Holds an array of references to the members of a Layer, each containing member IDs.

        :param data: The list of members who belong to this layer.
        :type data: [LayerRelationshipsMembersDataItems], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
