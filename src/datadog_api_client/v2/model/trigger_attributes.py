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
    from datadog_api_client.v2.model.monitor_alert_trigger_attributes import MonitorAlertTriggerAttributes
    from datadog_api_client.v2.model.trigger_type import TriggerType


class TriggerAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.monitor_alert_trigger_attributes import MonitorAlertTriggerAttributes
        from datadog_api_client.v2.model.trigger_type import TriggerType

        return {
            "monitor_alert_trigger": (MonitorAlertTriggerAttributes,),
            "type": (TriggerType,),
        }

    attribute_map = {
        "monitor_alert_trigger": "monitor_alert_trigger",
        "type": "type",
    }

    def __init__(self_, monitor_alert_trigger: MonitorAlertTriggerAttributes, type: TriggerType, **kwargs):
        """
        The trigger definition for starting an investigation.

        :param monitor_alert_trigger: Attributes for a monitor alert trigger.
        :type monitor_alert_trigger: MonitorAlertTriggerAttributes

        :param type: The type of trigger for the investigation.
        :type type: TriggerType
        """
        super().__init__(kwargs)

        self_.monitor_alert_trigger = monitor_alert_trigger
        self_.type = type
