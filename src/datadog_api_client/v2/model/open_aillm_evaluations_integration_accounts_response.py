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
    from datadog_api_client.v2.model.open_aillm_evaluations_integration_account_response_data import (
        OpenAILLMEvaluationsIntegrationAccountResponseData,
    )


class OpenAILLMEvaluationsIntegrationAccountsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.open_aillm_evaluations_integration_account_response_data import (
            OpenAILLMEvaluationsIntegrationAccountResponseData,
        )

        return {
            "data": ([OpenAILLMEvaluationsIntegrationAccountResponseData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[OpenAILLMEvaluationsIntegrationAccountResponseData], **kwargs):
        """
        Response payload for a list of OpenAI LLM Evaluations integration accounts.

        :param data: List of OpenAI LLM Evaluations integration accounts.
        :type data: [OpenAILLMEvaluationsIntegrationAccountResponseData]
        """
        super().__init__(kwargs)

        self_.data = data
