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
    from datadog_api_client.v1_20270101.model.timeseries_x_axis_date_format import TimeseriesXAxisDateFormat


class TimeseriesXAxis(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.timeseries_x_axis_date_format import TimeseriesXAxisDateFormat

        return {
            "date_format": (TimeseriesXAxisDateFormat,),
            "label": (str,),
        }

    attribute_map = {
        "date_format": "date_format",
        "label": "label",
    }

    def __init__(
        self_,
        date_format: Union[TimeseriesXAxisDateFormat, UnsetType] = unset,
        label: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param date_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type date_format: TimeseriesXAxisDateFormat, optional

        :param label: Test-only generated schema for the dashboard versioning proof of concept.
        :type label: str, optional
        """
        if date_format is not unset:
            kwargs["date_format"] = date_format
        if label is not unset:
            kwargs["label"] = label
        super().__init__(kwargs)
