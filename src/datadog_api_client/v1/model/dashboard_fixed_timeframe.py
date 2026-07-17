# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.dashboard_fixed_timeframe_type import DashboardFixedTimeframeType


class DashboardFixedTimeframe(ModelNormal):
    validations = {
        "_from": {
            "inclusive_minimum": 0,
        },
        "to": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.dashboard_fixed_timeframe_type import DashboardFixedTimeframeType

        return {
            "_from": (int,),
            "to": (int,),
            "type": (DashboardFixedTimeframeType,),
        }

    attribute_map = {
        "_from": "from",
        "to": "to",
        "type": "type",
    }

    def __init__(self_, _from: int, to: int, type: DashboardFixedTimeframeType, **kwargs):
        """
        A fixed dashboard timeframe.

        :param _from: Start time in milliseconds since epoch.
        :type _from: int

        :param to: End time in milliseconds since epoch.
        :type to: int

        :param type: Type of fixed timeframe.
        :type type: DashboardFixedTimeframeType
        """
        super().__init__(kwargs)

        self_._from = _from
        self_.to = to
        self_.type = type
