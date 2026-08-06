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
    from datadog_api_client.v2.model.notification_rule_target_configuration import NotificationRuleTargetConfiguration
    from datadog_api_client.v2.model.notification_rule_target_type import NotificationRuleTargetType


class NotificationRuleTarget(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.notification_rule_target_configuration import (
            NotificationRuleTargetConfiguration,
        )
        from datadog_api_client.v2.model.notification_rule_target_type import NotificationRuleTargetType

        return {
            "configuration": (NotificationRuleTargetConfiguration,),
            "type": (NotificationRuleTargetType,),
            "version": (int,),
        }

    attribute_map = {
        "configuration": "configuration",
        "type": "type",
        "version": "version",
    }

    def __init__(
        self_,
        configuration: NotificationRuleTargetConfiguration,
        type: NotificationRuleTargetType,
        version: int,
        **kwargs,
    ):
        """
        A notification target that receives change alerts for a feature flag.

        :param configuration: Configuration for a notification target. Which fields apply depends on the target's ``type``.
        :type configuration: NotificationRuleTargetConfiguration

        :param type: The type of notification target.
        :type type: NotificationRuleTargetType

        :param version: Schema version of ``configuration``.
        :type version: int
        """
        super().__init__(kwargs)

        self_.configuration = configuration
        self_.type = type
        self_.version = version
