# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_notification_rule_conditions_items import (
        IncidentNotificationRuleConditionsItems,
    )
    from datadog_api_client.v2.model.incident_notification_rule_attributes_visibility import (
        IncidentNotificationRuleAttributesVisibility,
    )


class IncidentNotificationRuleAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_notification_rule_conditions_items import (
            IncidentNotificationRuleConditionsItems,
        )
        from datadog_api_client.v2.model.incident_notification_rule_attributes_visibility import (
            IncidentNotificationRuleAttributesVisibility,
        )

        return {
            "conditions": ([IncidentNotificationRuleConditionsItems],),
            "created": (datetime,),
            "enabled": (bool,),
            "handles": ([str],),
            "modified": (datetime,),
            "renotify_on": ([str],),
            "trigger": (str,),
            "visibility": (IncidentNotificationRuleAttributesVisibility,),
        }

    attribute_map = {
        "conditions": "conditions",
        "created": "created",
        "enabled": "enabled",
        "handles": "handles",
        "modified": "modified",
        "renotify_on": "renotify_on",
        "trigger": "trigger",
        "visibility": "visibility",
    }
    read_only_vars = {
        "created",
        "modified",
    }

    def __init__(
        self_,
        conditions: List[IncidentNotificationRuleConditionsItems],
        created: datetime,
        enabled: bool,
        handles: List[str],
        modified: datetime,
        trigger: str,
        visibility: IncidentNotificationRuleAttributesVisibility,
        renotify_on: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        The notification rule's attributes.

        :param conditions: The conditions that trigger this notification rule.
        :type conditions: [IncidentNotificationRuleConditionsItems]

        :param created: Timestamp when the notification rule was created.
        :type created: datetime

        :param enabled: Whether the notification rule is enabled.
        :type enabled: bool

        :param handles: The notification handles (targets) for this rule.
        :type handles: [str]

        :param modified: Timestamp when the notification rule was last modified.
        :type modified: datetime

        :param renotify_on: List of incident fields that trigger re-notification when changed.
        :type renotify_on: [str], optional

        :param trigger: The trigger event for this notification rule.
        :type trigger: str

        :param visibility: The visibility of the notification rule.
        :type visibility: IncidentNotificationRuleAttributesVisibility
        """
        if renotify_on is not unset:
            kwargs["renotify_on"] = renotify_on
        super().__init__(kwargs)

        self_.conditions = conditions
        self_.created = created
        self_.enabled = enabled
        self_.handles = handles
        self_.modified = modified
        self_.trigger = trigger
        self_.visibility = visibility
