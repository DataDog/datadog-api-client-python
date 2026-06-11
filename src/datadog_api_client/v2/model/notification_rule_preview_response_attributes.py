# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.notification_rule_preview_result import NotificationRulePreviewResult


class NotificationRulePreviewResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.notification_rule_preview_result import NotificationRulePreviewResult

        return {
            "preview_results": ([NotificationRulePreviewResult],),
        }

    attribute_map = {
        "preview_results": "preview_results",
    }

    def __init__(self_, preview_results: List[NotificationRulePreviewResult], **kwargs):
        """
        Attributes of the notification preview response.

        :param preview_results: List of preview results for each rule type matched by the notification rule.
        :type preview_results: [NotificationRulePreviewResult]
        """
        super().__init__(kwargs)

        self_.preview_results = preview_results
