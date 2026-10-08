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
    from datadog_api_client.v2.model.monitor_automation_attributes import MonitorAutomationAttributes
    from datadog_api_client.v2.model.monitor_automation_type import MonitorAutomationType


class MonitorAutomationData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.monitor_automation_attributes import MonitorAutomationAttributes
        from datadog_api_client.v2.model.monitor_automation_type import MonitorAutomationType

        return {
            "attributes": (MonitorAutomationAttributes,),
            "id": (str,),
            "type": (MonitorAutomationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: MonitorAutomationAttributes, id: str, type: MonitorAutomationType, **kwargs):
        """
        Automatic investigation configuration identified by monitor ID.

        :param attributes: Automatic investigation settings for a monitor.
        :type attributes: MonitorAutomationAttributes

        :param id: The monitor ID.
        :type id: str

        :param type: The resource type for monitor automation settings.
        :type type: MonitorAutomationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
