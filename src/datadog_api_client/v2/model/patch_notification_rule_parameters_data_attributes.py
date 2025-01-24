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
    from datadog_api_client.v2.model.selectors import Selectors


class PatchNotificationRuleParametersDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.selectors import Selectors

        return {
            "enabled": (bool,),
            "name": (str,),
            "selectors": (Selectors,),
            "targets": ([str],),
            "time_aggregation": (int,),
            "version": (int,),
        }

    attribute_map = {
        "enabled": "enabled",
        "name": "name",
        "selectors": "selectors",
        "targets": "targets",
        "time_aggregation": "time_aggregation",
        "version": "version",
    }

    def __init__(
        self_,
        enabled: Union[bool, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        selectors: Union[Selectors, UnsetType] = unset,
        targets: Union[List[str], UnsetType] = unset,
        time_aggregation: Union[int, UnsetType] = unset,
        version: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the notification rule patch request. It is required to update the version of the rule when patching it.

        :param enabled: Field used to enable or disable the rule.
        :type enabled: bool, optional

        :param name: Name of the notification rule.
        :type name: str, optional

        :param selectors: Selectors are used to filter security issues for which notifications should be generated.
            Users can specify rule severities, rule types, a query to filter security issues on tags and attributes, and the trigger source.
            Only the trigger_source field is required.
        :type selectors: Selectors, optional

        :param targets: List of recipients to notify when a notification rule is triggered. Many different target types are supported,
            such as email addresses, Slack channels, and PagerDuty services.
            The appropriate integrations need to be properly configured to send notifications to the specified targets.
        :type targets: [str], optional

        :param time_aggregation: Time aggregation period (in seconds) is used to aggregate the results of the notification rule evaluation.
            Results are aggregated over a selected time frame using a rolling window, which updates with each new evaluation.
            Notifications are only sent for new issues discovered during the window.
            Time aggregation is only available for vulnerability-based notification rules. When omitted or set to 0, no aggregation
            is done.
        :type time_aggregation: int, optional

        :param version: Version of the notification rule. It is updated when the rule is modified.
        :type version: int, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if name is not unset:
            kwargs["name"] = name
        if selectors is not unset:
            kwargs["selectors"] = selectors
        if targets is not unset:
            kwargs["targets"] = targets
        if time_aggregation is not unset:
            kwargs["time_aggregation"] = time_aggregation
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
