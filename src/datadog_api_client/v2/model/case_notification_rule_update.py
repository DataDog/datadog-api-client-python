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
    from datadog_api_client.v2.model.case_notification_rule_attributes import CaseNotificationRuleAttributes
    from datadog_api_client.v2.model.case_notification_rule_resource_type import CaseNotificationRuleResourceType


class CaseNotificationRuleUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_notification_rule_attributes import CaseNotificationRuleAttributes
        from datadog_api_client.v2.model.case_notification_rule_resource_type import CaseNotificationRuleResourceType

        return {
            "attributes": (CaseNotificationRuleAttributes,),
            "type": (CaseNotificationRuleResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: CaseNotificationRuleResourceType,
        attributes: Union[CaseNotificationRuleAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Notification rule update

        :param attributes: Notification rule attributes
        :type attributes: CaseNotificationRuleAttributes, optional

        :param type: Notification rule resource type
        :type type: CaseNotificationRuleResourceType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
