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
    from datadog_api_client.v2.model.incident_notification_rule_conditions_items import (
        IncidentNotificationRuleConditionsItems,
    )
    from datadog_api_client.v2.model.incident_notification_rule_create_attributes_visibility import (
        IncidentNotificationRuleCreateAttributesVisibility,
    )


class IncidentNotificationRuleCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_notification_rule_conditions_items import (
            IncidentNotificationRuleConditionsItems,
        )
        from datadog_api_client.v2.model.incident_notification_rule_create_attributes_visibility import (
            IncidentNotificationRuleCreateAttributesVisibility,
        )

        return {
            "conditions": ([IncidentNotificationRuleConditionsItems],),
            "enabled": (bool,),
            "handles": ([str],),
            "renotify_on": ([str],),
            "trigger": (str,),
            "visibility": (IncidentNotificationRuleCreateAttributesVisibility,),
        }

    attribute_map = {
        "conditions": "conditions",
        "enabled": "enabled",
        "handles": "handles",
        "renotify_on": "renotify_on",
        "trigger": "trigger",
        "visibility": "visibility",
    }

    def __init__(
        self_,
        conditions: List[IncidentNotificationRuleConditionsItems],
        handles: List[str],
        trigger: str,
        enabled: Union[bool, UnsetType] = unset,
        renotify_on: Union[List[str], UnsetType] = unset,
        visibility: Union[IncidentNotificationRuleCreateAttributesVisibility, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes for creating a notification rule.

        :param conditions: The conditions that trigger this notification rule.
        :type conditions: [IncidentNotificationRuleConditionsItems]

        :param enabled: Whether the notification rule is enabled.
        :type enabled: bool, optional

        :param handles: The notification handles (targets) for this rule.
        :type handles: [str]

        :param renotify_on: List of incident fields that trigger re-notification when changed.
        :type renotify_on: [str], optional

        :param trigger: The trigger event for this notification rule.
        :type trigger: str

        :param visibility: The visibility of the notification rule.
        :type visibility: IncidentNotificationRuleCreateAttributesVisibility, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if renotify_on is not unset:
            kwargs["renotify_on"] = renotify_on
        if visibility is not unset:
            kwargs["visibility"] = visibility
        super().__init__(kwargs)

        self_.conditions = conditions
        self_.handles = handles
        self_.trigger = trigger
