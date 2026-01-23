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


class GlobalIncidentSettingsAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "analytics_dashboard_id": (str,),
        }

    attribute_map = {
        "analytics_dashboard_id": "analytics_dashboard_id",
    }

    def __init__(self_, analytics_dashboard_id: Union[str, UnsetType] = unset, **kwargs):
        """
        Global incident settings attributes

        :param analytics_dashboard_id: The analytics dashboard ID
        :type analytics_dashboard_id: str, optional
        """
        if analytics_dashboard_id is not unset:
            kwargs["analytics_dashboard_id"] = analytics_dashboard_id
        super().__init__(kwargs)
