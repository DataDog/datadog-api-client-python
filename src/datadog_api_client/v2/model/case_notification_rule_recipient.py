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
    from datadog_api_client.v2.model.case_notification_rule_recipient_data import CaseNotificationRuleRecipientData


class CaseNotificationRuleRecipient(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_notification_rule_recipient_data import CaseNotificationRuleRecipientData

        return {
            "data": (CaseNotificationRuleRecipientData,),
            "type": (str,),
        }

    attribute_map = {
        "data": "data",
        "type": "type",
    }

    def __init__(
        self_,
        data: Union[CaseNotificationRuleRecipientData, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Notification rule recipient

        :param data: Recipient data
        :type data: CaseNotificationRuleRecipientData, optional

        :param type: Type of recipient (SLACK_CHANNEL, EMAIL, HTTP, PAGERDUTY_SERVICE, MS_TEAMS_CHANNEL)
        :type type: str, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
