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
    from datadog_api_client.v2.model.patch_notification_rule_parameters_data_attributes import (
        PatchNotificationRuleParametersDataAttributes,
    )
    from datadog_api_client.v2.model.notification_rules_type import NotificationRulesType


class PatchNotificationRuleParametersData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.patch_notification_rule_parameters_data_attributes import (
            PatchNotificationRuleParametersDataAttributes,
        )
        from datadog_api_client.v2.model.notification_rules_type import NotificationRulesType

        return {
            "attributes": (PatchNotificationRuleParametersDataAttributes,),
            "id": (str,),
            "type": (NotificationRulesType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: PatchNotificationRuleParametersDataAttributes, id: str, type: NotificationRulesType, **kwargs
    ):
        """
        Data of the notification rule patch request: the rule ID, the rule type, and the rule attributes. All fields are required.

        :param attributes: Attributes of the notification rule patch request. It is required to update the version of the rule when patching it.
        :type attributes: PatchNotificationRuleParametersDataAttributes

        :param id: The ID of a notification rule.
        :type id: str

        :param type: The rule type associated to notification rules.
        :type type: NotificationRulesType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
