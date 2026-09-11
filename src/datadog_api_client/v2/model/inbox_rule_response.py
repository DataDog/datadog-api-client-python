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
    from datadog_api_client.v2.model.inbox_rule_data_response import InboxRuleDataResponse


class InboxRuleResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.inbox_rule_data_response import InboxRuleDataResponse

        return {
            "data": (InboxRuleDataResponse,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: InboxRuleDataResponse, **kwargs):
        """
        A single inbox rule response.

        :param data: The data object for an inbox rule returned by the API.
        :type data: InboxRuleDataResponse
        """
        super().__init__(kwargs)

        self_.data = data
