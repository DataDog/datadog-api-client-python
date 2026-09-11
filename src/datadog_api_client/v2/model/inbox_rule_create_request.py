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
    from datadog_api_client.v2.model.inbox_rule_data_create import InboxRuleDataCreate


class InboxRuleCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.inbox_rule_data_create import InboxRuleDataCreate

        return {
            "data": (InboxRuleDataCreate,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: InboxRuleDataCreate, **kwargs):
        """
        The body of an inbox rule create request.

        :param data: The data object for an inbox rule create request.
        :type data: InboxRuleDataCreate
        """
        super().__init__(kwargs)

        self_.data = data
