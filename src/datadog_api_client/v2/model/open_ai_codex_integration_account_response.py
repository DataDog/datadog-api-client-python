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
    from datadog_api_client.v2.model.open_ai_codex_integration_account_response_data import (
        OpenAICodexIntegrationAccountResponseData,
    )


class OpenAICodexIntegrationAccountResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.open_ai_codex_integration_account_response_data import (
            OpenAICodexIntegrationAccountResponseData,
        )

        return {
            "data": (OpenAICodexIntegrationAccountResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: OpenAICodexIntegrationAccountResponseData, **kwargs):
        """
        Response payload for a single OpenAI Codex integration account.

        :param data: Data envelope of an OpenAI Codex integration account, including server-assigned identity.
        :type data: OpenAICodexIntegrationAccountResponseData
        """
        super().__init__(kwargs)

        self_.data = data
