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
    from datadog_api_client.v2.model.overview_item_data_attributes import OverviewItemDataAttributes
    from datadog_api_client.v2.model.overview_item_data_type import OverviewItemDataType


class OverviewItemData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.overview_item_data_attributes import OverviewItemDataAttributes
        from datadog_api_client.v2.model.overview_item_data_type import OverviewItemDataType

        return {
            "attributes": (OverviewItemDataAttributes,),
            "id": (str,),
            "type": (OverviewItemDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: OverviewItemDataType,
        attributes: Union[OverviewItemDataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single tile entry in the End User Device Monitoring overview response.

        :param attributes: Attributes of a single tile in the End User Device Monitoring overview dashboard.
        :type attributes: OverviewItemDataAttributes, optional

        :param id: Unique identifier of the overview tile.
        :type id: str

        :param type: Overview items resource type.
        :type type: OverviewItemDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
