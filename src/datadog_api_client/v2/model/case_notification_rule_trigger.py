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
    from datadog_api_client.v2.model.case_notification_rule_trigger_data import CaseNotificationRuleTriggerData


class CaseNotificationRuleTrigger(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_notification_rule_trigger_data import CaseNotificationRuleTriggerData

        return {
            "data": (CaseNotificationRuleTriggerData,),
            "type": (str,),
        }

    attribute_map = {
        "data": "data",
        "type": "type",
    }

    def __init__(
        self_,
        data: Union[CaseNotificationRuleTriggerData, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Notification rule trigger

        :param data: Trigger data
        :type data: CaseNotificationRuleTriggerData, optional

        :param type: Type of trigger (CASE_CREATED, STATUS_TRANSITIONED, ATTRIBUTE_VALUE_CHANGED, EVENT_CORRELATION_SIGNAL_CORRELATED)
        :type type: str, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
