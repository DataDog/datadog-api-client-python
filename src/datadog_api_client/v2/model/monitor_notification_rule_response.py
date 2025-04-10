# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.monitor_notification_rule_data import MonitorNotificationRuleData
    from datadog_api_client.v2.model.monitor_notification_rule_response_included_item import (
        MonitorNotificationRuleResponseIncludedItem,
    )
    from datadog_api_client.v2.model.user import User


class MonitorNotificationRuleResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.monitor_notification_rule_data import MonitorNotificationRuleData
        from datadog_api_client.v2.model.monitor_notification_rule_response_included_item import (
            MonitorNotificationRuleResponseIncludedItem,
        )

        return {
            "data": (MonitorNotificationRuleData,),
            "included": ([MonitorNotificationRuleResponseIncludedItem],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: Union[MonitorNotificationRuleData, UnsetType] = unset,
        included: Union[List[Union[MonitorNotificationRuleResponseIncludedItem, User]], UnsetType] = unset,
        **kwargs,
    ):
        """
        A monitor notification rule.

        :param data: Monitor notification rule data.
        :type data: MonitorNotificationRuleData, optional

        :param included: Array of objects related to the monitor notification rule that the user requested.
        :type included: [MonitorNotificationRuleResponseIncludedItem], optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)
