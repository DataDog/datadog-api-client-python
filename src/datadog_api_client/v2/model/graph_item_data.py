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
    from datadog_api_client.v2.model.graph_item_data_attributes import GraphItemDataAttributes
    from datadog_api_client.v2.model.graph_item_data_type import GraphItemDataType


class GraphItemData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.graph_item_data_attributes import GraphItemDataAttributes
        from datadog_api_client.v2.model.graph_item_data_type import GraphItemDataType

        return {
            "attributes": (GraphItemDataAttributes,),
            "id": (str,),
            "type": (GraphItemDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, id: str, type: GraphItemDataType, attributes: Union[GraphItemDataAttributes, UnsetType] = unset, **kwargs
    ):
        """
        A single grouping entry in the End User Device Monitoring graph response.

        :param attributes: Attributes of a single grouping in the End User Device Monitoring graph response.
        :type attributes: GraphItemDataAttributes, optional

        :param id: Unique identifier of the grouping, derived from the grouping column.
        :type id: str

        :param type: Graph items resource type.
        :type type: GraphItemDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
