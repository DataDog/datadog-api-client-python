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
    from datadog_api_client.v2.model.maintenance_window_create import MaintenanceWindowCreate


class MaintenanceWindowCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.maintenance_window_create import MaintenanceWindowCreate

        return {
            "data": (MaintenanceWindowCreate,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: MaintenanceWindowCreate, **kwargs):
        """
        Request payload for creating a maintenance window.

        :param data: Data object for creating a maintenance window.
        :type data: MaintenanceWindowCreate
        """
        super().__init__(kwargs)

        self_.data = data
