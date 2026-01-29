# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MonitorNotificationRuleCondition(ModelNormal):
    validations = {
        "recipients": {
            "max_items": 20,
            "min_items": 1,
        },
        "scope": {
            "max_length": 3000,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "recipients": ([str],),
            "scope": (str,),
        }

    attribute_map = {
        "recipients": "recipients",
        "scope": "scope",
    }

    def __init__(self_, recipients: List[str], scope: str, **kwargs):
        """
        A conditional recipient rule composed of a ``scope`` (the matching condition) and
        ``recipients`` (who to notify when it matches).

        :param recipients: A list of recipients to notify. Uses the same format as the monitor ``message`` field. Must not start with an '@'. Cannot be used with ``conditional_recipients``.
        :type recipients: [str]

        :param scope: Defines the condition under which the recipients are notified. Supported formats:

            * Monitor status condition using ``transition_type:<status>`` , for example ``transition_type:is_alert``.
            * A single tag key:value pair, for example ``env:prod``.
        :type scope: str
        """
        super().__init__(kwargs)

        self_.recipients = recipients
        self_.scope = scope
