# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_custom_rule_revision_response_data import AiCustomRuleRevisionResponseData


class AiCustomRuleRevisionsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_custom_rule_revision_response_data import AiCustomRuleRevisionResponseData

        return {
            "data": ([AiCustomRuleRevisionResponseData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[AiCustomRuleRevisionResponseData], **kwargs):
        """
        Response containing a list of AI custom rule revisions.

        :param data: The list of AI custom rule revisions.
        :type data: [AiCustomRuleRevisionResponseData]
        """
        super().__init__(kwargs)

        self_.data = data
