# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.notification_rule_preview_response_attributes import (
        NotificationRulePreviewResponseAttributes,
    )
    from datadog_api_client.v2.model.notification_rule_preview_response_type import NotificationRulePreviewResponseType


class NotificationRulePreviewResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.notification_rule_preview_response_attributes import (
            NotificationRulePreviewResponseAttributes,
        )
        from datadog_api_client.v2.model.notification_rule_preview_response_type import (
            NotificationRulePreviewResponseType,
        )

        return {
            "attributes": (NotificationRulePreviewResponseAttributes,),
            "id": (str,),
            "type": (NotificationRulePreviewResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: NotificationRulePreviewResponseAttributes,
        type: NotificationRulePreviewResponseType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The notification preview response data.

        :param attributes: Attributes of the notification preview response.
        :type attributes: NotificationRulePreviewResponseAttributes

        :param id: The ID of the notification preview response.
        :type id: str, optional

        :param type: The type of the notification preview response.
        :type type: NotificationRulePreviewResponseType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
