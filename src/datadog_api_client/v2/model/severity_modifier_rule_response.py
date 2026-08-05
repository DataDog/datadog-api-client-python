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
    from datadog_api_client.v2.model.severity_modifier_rule_data_response import SeverityModifierRuleDataResponse


class SeverityModifierRuleResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.severity_modifier_rule_data_response import SeverityModifierRuleDataResponse

        return {
            "data": (SeverityModifierRuleDataResponse,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SeverityModifierRuleDataResponse, **kwargs):
        """
        A single severity modifier rule response.

        :param data: The data object for a severity modifier rule as returned by the API.
        :type data: SeverityModifierRuleDataResponse
        """
        super().__init__(kwargs)

        self_.data = data
