# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class StructuredAnalysisTimeAggregation(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "interval": (float,),
            "time_column": (str,),
        }

    attribute_map = {
        "interval": "interval",
        "time_column": "time_column",
    }

    def __init__(self_, time_column: str, interval: Union[float, UnsetType] = unset, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param interval: Test-only generated schema for the dashboard versioning proof of concept.
        :type interval: float, optional

        :param time_column: Test-only generated schema for the dashboard versioning proof of concept.
        :type time_column: str
        """
        if interval is not unset:
            kwargs["interval"] = interval
        super().__init__(kwargs)

        self_.time_column = time_column
