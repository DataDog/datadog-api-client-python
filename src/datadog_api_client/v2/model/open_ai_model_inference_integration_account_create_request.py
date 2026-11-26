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
    from datadog_api_client.v2.model.open_ai_model_inference_integration_account_create_data import (
        OpenAIModelInferenceIntegrationAccountCreateData,
    )


class OpenAIModelInferenceIntegrationAccountCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.open_ai_model_inference_integration_account_create_data import (
            OpenAIModelInferenceIntegrationAccountCreateData,
        )

        return {
            "data": (OpenAIModelInferenceIntegrationAccountCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: OpenAIModelInferenceIntegrationAccountCreateData, **kwargs):
        """
        Request payload to create an OpenAI Model Inference integration account.

        :param data: Data envelope for creating an OpenAI Model Inference integration account.
        :type data: OpenAIModelInferenceIntegrationAccountCreateData
        """
        super().__init__(kwargs)

        self_.data = data
