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
    from datadog_api_client.v2.model.notification_rule_preview_notification_status import (
        NotificationRulePreviewNotificationStatus,
    )
    from datadog_api_client.v2.model.rule_types_items import RuleTypesItems


class NotificationRulePreviewResult(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.notification_rule_preview_notification_status import (
            NotificationRulePreviewNotificationStatus,
        )
        from datadog_api_client.v2.model.rule_types_items import RuleTypesItems

        return {
            "notification_status": (NotificationRulePreviewNotificationStatus,),
            "rule_type": (RuleTypesItems,),
        }

    attribute_map = {
        "notification_status": "notification_status",
        "rule_type": "rule_type",
    }

    def __init__(
        self_, notification_status: NotificationRulePreviewNotificationStatus, rule_type: RuleTypesItems, **kwargs
    ):
        """
        The preview result for a single rule type.

        :param notification_status: The notification status for the given rule type. ``SUCCESS`` means a matching event was found and the notification was sent successfully. ``DEFAULT`` means no matching event was found and a default placeholder notification was sent instead. ``ERROR`` means an error occurred while sending the notification.
        :type notification_status: NotificationRulePreviewNotificationStatus

        :param rule_type: Security rule type which can be used in security rules.
            Signal-based notification rules can filter signals based on rule types application_security, log_detection,
            workload_security, signal_correlation, cloud_configuration and infrastructure_configuration.
            Vulnerability-based notification rules can filter vulnerabilities based on rule types application_code_vulnerability,
            application_library_vulnerability, attack_path, container_image_vulnerability, identity_risk, misconfiguration,
            api_security, host_vulnerability, iac_misconfiguration, sast_vulnerability, secret_vulnerability and workload_activity.
        :type rule_type: RuleTypesItems
        """
        super().__init__(kwargs)

        self_.notification_status = notification_status
        self_.rule_type = rule_type
