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
    from datadog_api_client.v2.model.create_notification_rule_parameters_data_attributes import (
        CreateNotificationRuleParametersDataAttributes,
    )
    from datadog_api_client.v2.model.notification_rules_type import NotificationRulesType


class CreateNotificationRuleParametersData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_notification_rule_parameters_data_attributes import (
            CreateNotificationRuleParametersDataAttributes,
        )
        from datadog_api_client.v2.model.notification_rules_type import NotificationRulesType

        return {
            "attributes": (CreateNotificationRuleParametersDataAttributes,),
            "type": (NotificationRulesType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: CreateNotificationRuleParametersDataAttributes, type: NotificationRulesType, **kwargs
    ):
        """
        Data of the notification rule create request: the rule type, and the rule attributes. All fields are required.

        :param attributes: Attributes of the notification rule create request.
        :type attributes: CreateNotificationRuleParametersDataAttributes

        :param type: The rule type associated to notification rules.
        :type type: NotificationRulesType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
