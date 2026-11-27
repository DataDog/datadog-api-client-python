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
    from datadog_api_client.v2.model.open_ai_model_inference_integration_account_authentication_request import (
        OpenAIModelInferenceIntegrationAccountAuthenticationRequest,
    )
    from datadog_api_client.v2.model.open_ai_model_inference_integration_dataflows_request import (
        OpenAIModelInferenceIntegrationDataflowsRequest,
    )
    from datadog_api_client.v2.model.open_ai_model_inference_integration_account_settings_request import (
        OpenAIModelInferenceIntegrationAccountSettingsRequest,
    )
    from datadog_api_client.v2.model.open_ai_model_inference_integration_account_bearer_token_auth_request import (
        OpenAIModelInferenceIntegrationAccountBearerTokenAuthRequest,
    )


class OpenAIModelInferenceIntegrationAccountCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.open_ai_model_inference_integration_account_authentication_request import (
            OpenAIModelInferenceIntegrationAccountAuthenticationRequest,
        )
        from datadog_api_client.v2.model.open_ai_model_inference_integration_dataflows_request import (
            OpenAIModelInferenceIntegrationDataflowsRequest,
        )
        from datadog_api_client.v2.model.open_ai_model_inference_integration_account_settings_request import (
            OpenAIModelInferenceIntegrationAccountSettingsRequest,
        )

        return {
            "authentication": (OpenAIModelInferenceIntegrationAccountAuthenticationRequest,),
            "dataflows": (OpenAIModelInferenceIntegrationDataflowsRequest,),
            "name": (str,),
            "settings": (OpenAIModelInferenceIntegrationAccountSettingsRequest,),
        }

    attribute_map = {
        "authentication": "authentication",
        "dataflows": "dataflows",
        "name": "name",
        "settings": "settings",
    }

    def __init__(
        self_,
        authentication: Union[
            OpenAIModelInferenceIntegrationAccountAuthenticationRequest,
            OpenAIModelInferenceIntegrationAccountBearerTokenAuthRequest,
        ],
        name: str,
        settings: OpenAIModelInferenceIntegrationAccountSettingsRequest,
        dataflows: Union[OpenAIModelInferenceIntegrationDataflowsRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Writable attributes used to create an OpenAI Model Inference integration account.

        :param authentication: Authentication for creating the OpenAI Model Inference integration account. Set exactly one method.
        :type authentication: OpenAIModelInferenceIntegrationAccountAuthenticationRequest

        :param dataflows: Data Datadog collects from OpenAI Model Inference, keyed by dataflow ID. Each dataflow turns on a distinct type of collection. Set ``enabled`` to start or stop a dataflow. The default for each dataflow applies when the account is created. On update, omitted fields keep their current values.
        :type dataflows: OpenAIModelInferenceIntegrationDataflowsRequest, optional

        :param name: Human-readable name of the OpenAI Model Inference integration account.
        :type name: str

        :param settings: Settings for creating the OpenAI Model Inference integration account.
        :type settings: OpenAIModelInferenceIntegrationAccountSettingsRequest
        """
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        super().__init__(kwargs)

        self_.authentication = authentication
        self_.name = name
        self_.settings = settings
