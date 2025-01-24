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
    from datadog_api_client.v2.model.rule_user import RuleUser
    from datadog_api_client.v2.model.selectors import Selectors


class NotificationRuleAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rule_user import RuleUser
        from datadog_api_client.v2.model.selectors import Selectors

        return {
            "created_at": (int,),
            "created_by": (RuleUser,),
            "enabled": (bool,),
            "modified_at": (int,),
            "modified_by": (RuleUser,),
            "name": (str,),
            "selectors": (Selectors,),
            "targets": ([str],),
            "time_aggregation": (int,),
            "version": (int,),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "enabled": "enabled",
        "modified_at": "modified_at",
        "modified_by": "modified_by",
        "name": "name",
        "selectors": "selectors",
        "targets": "targets",
        "time_aggregation": "time_aggregation",
        "version": "version",
    }

    def __init__(
        self_,
        created_at: int,
        created_by: RuleUser,
        enabled: bool,
        modified_at: int,
        modified_by: RuleUser,
        name: str,
        selectors: Selectors,
        targets: List[str],
        version: int,
        time_aggregation: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the notification rule.

        :param created_at: Date as Unix timestamp in milliseconds.
        :type created_at: int

        :param created_by: User creating or modifying a rule.
        :type created_by: RuleUser

        :param enabled: Field used to enable or disable the rule.
        :type enabled: bool

        :param modified_at: Date as Unix timestamp in milliseconds.
        :type modified_at: int

        :param modified_by: User creating or modifying a rule.
        :type modified_by: RuleUser

        :param name: Name of the notification rule.
        :type name: str

        :param selectors: Selectors are used to filter security issues for which notifications should be generated.
            Users can specify rule severities, rule types, a query to filter security issues on tags and attributes, and the trigger source.
            Only the trigger_source field is required.
        :type selectors: Selectors

        :param targets: List of recipients to notify when a notification rule is triggered. Many different target types are supported,
            such as email addresses, Slack channels, and PagerDuty services.
            The appropriate integrations need to be properly configured to send notifications to the specified targets.
        :type targets: [str]

        :param time_aggregation: Time aggregation period (in seconds) is used to aggregate the results of the notification rule evaluation.
            Results are aggregated over a selected time frame using a rolling window, which updates with each new evaluation.
            Notifications are only sent for new issues discovered during the window.
            Time aggregation is only available for vulnerability-based notification rules. When omitted or set to 0, no aggregation
            is done.
        :type time_aggregation: int, optional

        :param version: Version of the notification rule. It is updated when the rule is modified.
        :type version: int
        """
        if time_aggregation is not unset:
            kwargs["time_aggregation"] = time_aggregation
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.created_by = created_by
        self_.enabled = enabled
        self_.modified_at = modified_at
        self_.modified_by = modified_by
        self_.name = name
        self_.selectors = selectors
        self_.targets = targets
        self_.version = version
