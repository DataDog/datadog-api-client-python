# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.layer_attributes_interval import LayerAttributesInterval
    from datadog_api_client.v2.model.time_restriction import TimeRestriction


class LayerAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.layer_attributes_interval import LayerAttributesInterval
        from datadog_api_client.v2.model.time_restriction import TimeRestriction

        return {
            "effective_date": (datetime,),
            "end_date": (datetime,),
            "interval": (LayerAttributesInterval,),
            "name": (str,),
            "restrictions": ([TimeRestriction],),
            "rotation_start": (datetime,),
        }

    attribute_map = {
        "effective_date": "effective_date",
        "end_date": "end_date",
        "interval": "interval",
        "name": "name",
        "restrictions": "restrictions",
        "rotation_start": "rotation_start",
    }

    def __init__(
        self_,
        effective_date: Union[datetime, UnsetType] = unset,
        end_date: Union[datetime, UnsetType] = unset,
        interval: Union[LayerAttributesInterval, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        restrictions: Union[List[TimeRestriction], UnsetType] = unset,
        rotation_start: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        Describes key properties of a Layer, including rotation details, name, start/end times, and any restrictions.

        :param effective_date: When the layer becomes active (ISO 8601).
        :type effective_date: datetime, optional

        :param end_date: When the layer ceases to be active (ISO 8601).
        :type end_date: datetime, optional

        :param interval: Defines how often the rotation repeats, using a combination of days and optional seconds. Should be at least 1 hour.
        :type interval: LayerAttributesInterval, optional

        :param name: The name of this layer.
        :type name: str, optional

        :param restrictions: An optional list of time restrictions for when this layer is in effect.
        :type restrictions: [TimeRestriction], optional

        :param rotation_start: The date/time when the rotation starts (ISO 8601).
        :type rotation_start: datetime, optional
        """
        if effective_date is not unset:
            kwargs["effective_date"] = effective_date
        if end_date is not unset:
            kwargs["end_date"] = end_date
        if interval is not unset:
            kwargs["interval"] = interval
        if name is not unset:
            kwargs["name"] = name
        if restrictions is not unset:
            kwargs["restrictions"] = restrictions
        if rotation_start is not unset:
            kwargs["rotation_start"] = rotation_start
        super().__init__(kwargs)
