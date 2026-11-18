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


class ProductAnalyticsMonitorUnlinkAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "chart_id": (str,),
            "dashboard_id": (str,),
        }

    attribute_map = {
        "chart_id": "chart_id",
        "dashboard_id": "dashboard_id",
    }

    def __init__(self_, chart_id: str, dashboard_id: Union[str, UnsetType] = unset, **kwargs):
        """
        The chart link to remove. It must match the stored link exactly:
        ``chart_id`` alone for a saved chart, or ``chart_id`` and ``dashboard_id`` for a dashboard widget.

        :param chart_id: ID of the chart the monitor is linked to.
        :type chart_id: str

        :param dashboard_id: ID of the dashboard the monitor is linked to.
        :type dashboard_id: str, optional
        """
        if dashboard_id is not unset:
            kwargs["dashboard_id"] = dashboard_id
        super().__init__(kwargs)

        self_.chart_id = chart_id
