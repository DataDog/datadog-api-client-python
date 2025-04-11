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
    from datadog_api_client.v2.model.layer_attributes_restrictions_items_end_day import (
        LayerAttributesRestrictionsItemsEndDay,
    )
    from datadog_api_client.v2.model.layer_attributes_restrictions_items_start_day import (
        LayerAttributesRestrictionsItemsStartDay,
    )


class LayerAttributesRestrictionsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.layer_attributes_restrictions_items_end_day import (
            LayerAttributesRestrictionsItemsEndDay,
        )
        from datadog_api_client.v2.model.layer_attributes_restrictions_items_start_day import (
            LayerAttributesRestrictionsItemsStartDay,
        )

        return {
            "end_day": (LayerAttributesRestrictionsItemsEndDay,),
            "end_time": (str,),
            "start_day": (LayerAttributesRestrictionsItemsStartDay,),
            "start_time": (str,),
        }

    attribute_map = {
        "end_day": "end_day",
        "end_time": "end_time",
        "start_day": "start_day",
        "start_time": "start_time",
    }

    def __init__(
        self_,
        end_day: Union[LayerAttributesRestrictionsItemsEndDay, UnsetType] = unset,
        end_time: Union[str, UnsetType] = unset,
        start_day: Union[LayerAttributesRestrictionsItemsStartDay, UnsetType] = unset,
        start_time: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Represents a time restriction within a layer, specifying the days and times
        when this layer is active or inactive.

        :param end_day: Defines the end day of the restriction within a Layer.
        :type end_day: LayerAttributesRestrictionsItemsEndDay, optional

        :param end_time: The time of day the restriction ends (hh:mm:ss).
        :type end_time: str, optional

        :param start_day: Defines the start day of the restriction within a Layer.
        :type start_day: LayerAttributesRestrictionsItemsStartDay, optional

        :param start_time: The time of day the restriction begins (hh:mm:ss).
        :type start_time: str, optional
        """
        if end_day is not unset:
            kwargs["end_day"] = end_day
        if end_time is not unset:
            kwargs["end_time"] = end_time
        if start_day is not unset:
            kwargs["start_day"] = start_day
        if start_time is not unset:
            kwargs["start_time"] = start_time
        super().__init__(kwargs)
