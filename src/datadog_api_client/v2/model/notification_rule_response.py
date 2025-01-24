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
    from datadog_api_client.v2.model.notification_rule import NotificationRule


class NotificationRuleResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.notification_rule import NotificationRule

        return {
            "data": (NotificationRule,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[NotificationRule, UnsetType] = unset, **kwargs):
        """
        Response object which includes a notification rule.

        :param data: Notification rules allow full control over notifications generated by the various Datadog security products.
            They allow users to define the conditions under which a notification should be generated (based on rule severities,
            rule types, rule tags, and so on), and the targets to notify.
            A notification rule is composed of a rule ID, a rule type, and the rule attributes. All fields are required.
        :type data: NotificationRule, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
