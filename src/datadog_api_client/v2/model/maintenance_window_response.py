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
    from datadog_api_client.v2.model.maintenance_window import MaintenanceWindow


class MaintenanceWindowResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.maintenance_window import MaintenanceWindow

        return {
            "data": (MaintenanceWindow,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: MaintenanceWindow, **kwargs):
        """
        Response containing a single maintenance window.

        :param data: A maintenance window that defines a scheduled time period during which case-related notifications and automation rules are suppressed. Each maintenance window applies to cases matching a specified query.
        :type data: MaintenanceWindow
        """
        super().__init__(kwargs)

        self_.data = data
