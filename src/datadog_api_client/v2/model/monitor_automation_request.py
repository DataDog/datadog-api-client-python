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
    from datadog_api_client.v2.model.monitor_automation_request_data import MonitorAutomationRequestData


class MonitorAutomationRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.monitor_automation_request_data import MonitorAutomationRequestData

        return {
            "data": (MonitorAutomationRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: MonitorAutomationRequestData, **kwargs):
        """
        Set whether Bits automatically investigates alerts from a monitor.

        :param data: The automatic investigation settings to apply.
        :type data: MonitorAutomationRequestData
        """
        super().__init__(kwargs)

        self_.data = data
