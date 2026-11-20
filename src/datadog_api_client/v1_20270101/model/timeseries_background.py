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
    from datadog_api_client.v1_20270101.model.timeseries_background_type import TimeseriesBackgroundType
    from datadog_api_client.v1_20270101.model.axis import Axis


class TimeseriesBackground(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.timeseries_background_type import TimeseriesBackgroundType
        from datadog_api_client.v1_20270101.model.axis import Axis

        return {
            "type": (TimeseriesBackgroundType,),
            "yaxis": (Axis,),
        }

    attribute_map = {
        "type": "type",
        "yaxis": "yaxis",
    }

    def __init__(self_, type: TimeseriesBackgroundType, yaxis: Union[Axis, UnsetType] = unset, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: TimeseriesBackgroundType

        :param yaxis: Test-only generated schema for the dashboard versioning proof of concept.
        :type yaxis: Axis, optional
        """
        if yaxis is not unset:
            kwargs["yaxis"] = yaxis
        super().__init__(kwargs)

        self_.type = type
