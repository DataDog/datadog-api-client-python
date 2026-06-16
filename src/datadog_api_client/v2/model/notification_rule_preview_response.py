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
    from datadog_api_client.v2.model.notification_rule_preview_response_data import NotificationRulePreviewResponseData


class NotificationRulePreviewResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.notification_rule_preview_response_data import (
            NotificationRulePreviewResponseData,
        )

        return {
            "data": (NotificationRulePreviewResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: NotificationRulePreviewResponseData, **kwargs):
        """
        Response from the notification preview request.

        :param data: The notification preview response data.
        :type data: NotificationRulePreviewResponseData
        """
        super().__init__(kwargs)

        self_.data = data
