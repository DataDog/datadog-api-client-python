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
    from datadog_api_client.v2.model.ai_custom_ruleset_response_data import AiCustomRulesetResponseData


class AiCustomRulesetResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_custom_ruleset_response_data import AiCustomRulesetResponseData

        return {
            "data": (AiCustomRulesetResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: AiCustomRulesetResponseData, **kwargs):
        """
        Response containing a single AI custom ruleset.

        :param data: Response data for an AI custom ruleset.
        :type data: AiCustomRulesetResponseData
        """
        super().__init__(kwargs)

        self_.data = data
