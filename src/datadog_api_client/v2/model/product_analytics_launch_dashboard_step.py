# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class ProductAnalyticsLaunchDashboardStep(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "dashboard_id": (str, none_type),
        }

    attribute_map = {
        "dashboard_id": "dashboard_id",
    }

    def __init__(self_, dashboard_id: Union[str, none_type, UnsetType] = unset, **kwargs):
        """
        Dashboard linked to the launch.

        :param dashboard_id: ID of the linked dashboard.
        :type dashboard_id: str, none_type, optional
        """
        if dashboard_id is not unset:
            kwargs["dashboard_id"] = dashboard_id
        super().__init__(kwargs)
