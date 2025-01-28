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
    from datadog_api_client.v2.model.inbox_rule import InboxRule


class InboxRuleResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.inbox_rule import InboxRule

        return {
            "data": (InboxRule,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[InboxRule, UnsetType] = unset, **kwargs):
        """
        Response object which includes an inbox rule.

        :param data: Inbox rules are used to prioritize and add relevant vulnerabilities to your Security Inbox.
            An inbox rule is composed of a rule UUID, a rule type, and the rule attributes. All fields are required.
        :type data: InboxRule, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
