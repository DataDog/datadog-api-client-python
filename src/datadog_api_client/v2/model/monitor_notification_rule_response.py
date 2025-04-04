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
    from datadog_api_client.v2.model.monitor_notification_rule_data import MonitorNotificationRuleData


class MonitorNotificationRuleResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.monitor_notification_rule_data import MonitorNotificationRuleData

        return {
            "data": (MonitorNotificationRuleData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[MonitorNotificationRuleData, UnsetType] = unset, **kwargs):
        """
        A monitor notification rule.

        :param data: Monitor notification rule data.
        :type data: MonitorNotificationRuleData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
