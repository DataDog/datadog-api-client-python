# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class TriggerAttributes(ModelComposed):
    def __init__(self, **kwargs):
        """
        The trigger definition for starting an investigation.

        :param monitor_alert_trigger: Attributes for a monitor alert trigger.
        :type monitor_alert_trigger: MonitorAlertTriggerAttributes

        :param type: The type of monitor alert trigger.
        :type type: MonitorAlertTriggerType

        :param general_investigation: Attributes for a general investigation, not tied to a specific monitor alert.
        :type general_investigation: GeneralInvestigationAttributes
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.monitor_alert_trigger import MonitorAlertTrigger
        from datadog_api_client.v2.model.general_investigation_trigger import GeneralInvestigationTrigger

        return {
            "oneOf": [
                MonitorAlertTrigger,
                GeneralInvestigationTrigger,
            ],
        }
