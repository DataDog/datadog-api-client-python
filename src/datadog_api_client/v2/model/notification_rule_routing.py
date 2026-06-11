# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.notification_rule_routing_mode import NotificationRuleRoutingMode


class NotificationRuleRouting(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.notification_rule_routing_mode import NotificationRuleRoutingMode

        return {
            "mode": (NotificationRuleRoutingMode,),
        }

    attribute_map = {
        "mode": "mode",
    }

    def __init__(self_, mode: NotificationRuleRoutingMode, **kwargs):
        """
        Routing configuration for the notification rule.

        :param mode: The routing mode for the notification rule. ``manual`` sends notifications to the configured targets.
        :type mode: NotificationRuleRoutingMode
        """
        super().__init__(kwargs)

        self_.mode = mode
