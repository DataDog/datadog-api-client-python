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
    from datadog_api_client.v2.model.case_notification_rule_create_attributes import (
        CaseNotificationRuleCreateAttributes,
    )
    from datadog_api_client.v2.model.case_notification_rule_resource_type import CaseNotificationRuleResourceType


class CaseNotificationRuleCreate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_notification_rule_create_attributes import (
            CaseNotificationRuleCreateAttributes,
        )
        from datadog_api_client.v2.model.case_notification_rule_resource_type import CaseNotificationRuleResourceType

        return {
            "attributes": (CaseNotificationRuleCreateAttributes,),
            "type": (CaseNotificationRuleResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: CaseNotificationRuleCreateAttributes, type: CaseNotificationRuleResourceType, **kwargs
    ):
        """
        Notification rule create

        :param attributes: Notification rule creation attributes
        :type attributes: CaseNotificationRuleCreateAttributes

        :param type: Notification rule resource type
        :type type: CaseNotificationRuleResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
