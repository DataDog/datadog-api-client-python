# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.general_investigation_attributes import GeneralInvestigationAttributes
    from datadog_api_client.v2.model.monitor_alert_trigger_attributes import MonitorAlertTriggerAttributes
    from datadog_api_client.v2.model.trigger_type import TriggerType
    from datadog_api_client.v2.model.general_investigation_attributes_without_time_bounds import (
        GeneralInvestigationAttributesWithoutTimeBounds,
    )
    from datadog_api_client.v2.model.general_investigation_attributes_with_time_bounds import (
        GeneralInvestigationAttributesWithTimeBounds,
    )


class TriggerAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.general_investigation_attributes import GeneralInvestigationAttributes
        from datadog_api_client.v2.model.monitor_alert_trigger_attributes import MonitorAlertTriggerAttributes
        from datadog_api_client.v2.model.trigger_type import TriggerType

        return {
            "general_investigation": (GeneralInvestigationAttributes,),
            "monitor_alert_trigger": (MonitorAlertTriggerAttributes,),
            "type": (TriggerType,),
        }

    attribute_map = {
        "general_investigation": "general_investigation",
        "monitor_alert_trigger": "monitor_alert_trigger",
        "type": "type",
    }

    def __init__(
        self_,
        general_investigation: Union[
            GeneralInvestigationAttributes,
            GeneralInvestigationAttributesWithoutTimeBounds,
            GeneralInvestigationAttributesWithTimeBounds,
            UnsetType,
        ] = unset,
        monitor_alert_trigger: Union[MonitorAlertTriggerAttributes, UnsetType] = unset,
        type: Union[TriggerType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The trigger definition for starting an investigation.

        :param general_investigation: Attributes for a general investigation, not tied to a specific monitor alert.
        :type general_investigation: GeneralInvestigationAttributes, optional

        :param monitor_alert_trigger: Attributes for a monitor alert trigger.
        :type monitor_alert_trigger: MonitorAlertTriggerAttributes, optional

        :param type: The type of trigger for the investigation.
        :type type: TriggerType, optional
        """
        if general_investigation is not unset:
            kwargs["general_investigation"] = general_investigation
        if monitor_alert_trigger is not unset:
            kwargs["monitor_alert_trigger"] = monitor_alert_trigger
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
