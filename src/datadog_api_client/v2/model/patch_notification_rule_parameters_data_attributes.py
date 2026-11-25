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
    from datadog_api_client.v2.model.notification_rule_routing import NotificationRuleRouting
    from datadog_api_client.v2.model.selectors import Selectors


class PatchNotificationRuleParametersDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.notification_rule_routing import NotificationRuleRouting
        from datadog_api_client.v2.model.selectors import Selectors

        return {
            "enabled": (bool,),
            "name": (str,),
            "routing": (NotificationRuleRouting,),
            "selectors": (Selectors,),
            "targets": ([str],),
            "time_aggregation": (int,),
            "version": (int,),
        }

    attribute_map = {
        "enabled": "enabled",
        "name": "name",
        "routing": "routing",
        "selectors": "selectors",
        "targets": "targets",
        "time_aggregation": "time_aggregation",
        "version": "version",
    }

    def __init__(
        self_,
        enabled: Union[bool, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        routing: Union[NotificationRuleRouting, UnsetType] = unset,
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

        :param name: Name of the notification rule. At most 500 characters, and unique in the organization (case-insensitive).
        :type name: str, optional

        :param routing: Routing configuration for the notification rule.
        :type routing: NotificationRuleRouting, optional

        :param selectors: Selectors are used to filter security issues for which notifications should be generated.
            Users can specify rule severities, rule types, a query to filter security issues on tags and attributes, and the trigger source.
            Only the trigger_source field is required.
        :type selectors: Selectors, optional

        :param targets: List of recipients to notify when a notification rule is triggered. Many different target types are supported,
            such as email addresses, Slack channels, and PagerDuty services.
            The appropriate integrations need to be properly configured to send notifications to the specified targets.
            Each target is a handle that starts with ``@``. Use ``@<EMAIL>`` for an email address
            (for example, ``@john.doe@email.com`` ), and ``@<INTEGRATION_NAME>-<VALUES>`` for an integration, such as
            ``@slack-<VALUES>`` , ``@pagerduty-<VALUES>`` , ``@jira-<VALUES>`` , ``@teams-<VALUES>`` , ``@servicenow-<VALUES>`` ,
            or ``@webhook-<WEBHOOK_NAME>``.
            Handles that include parentheses are not supported.
            A rule can have at most 20 targets, each at most 500 characters long. Finding-based rules don't accept
            ``case`` , ``incident`` , ``jira`` , or ``linear`` targets; use an automatic ticket creation rule for cases,
            Jira, and Linear.
        :type targets: [str], optional

        :param time_aggregation: Time aggregation period (in seconds) is used to aggregate the results of the notification rule evaluation.
            Results are aggregated over a selected time frame using a rolling window, which updates with each new evaluation.
            Notifications are only sent for new issues discovered during the window.
            Time aggregation is only available for finding-based notification rules. When omitted or set to 0, no aggregation
            is done. Otherwise, it must be between 1800 (30 minutes) and 2592000 (30 days).
        :type time_aggregation: int, optional

        :param version: Version of the notification rule. It is updated when the rule is modified.
            When patching a rule, send the current ``version`` returned by the get or list operation; an older
            ``version`` returns 409.
        :type version: int, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if name is not unset:
            kwargs["name"] = name
        if routing is not unset:
            kwargs["routing"] = routing
        if selectors is not unset:
            kwargs["selectors"] = selectors
        if targets is not unset:
            kwargs["targets"] = targets
        if time_aggregation is not unset:
            kwargs["time_aggregation"] = time_aggregation
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
