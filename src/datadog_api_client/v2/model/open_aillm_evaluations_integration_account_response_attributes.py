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
    from datadog_api_client.v2.model.open_aillm_evaluations_integration_account_authentication_response import (
        OpenAILLMEvaluationsIntegrationAccountAuthenticationResponse,
    )
    from datadog_api_client.v2.model.open_aillm_evaluations_integration_dataflows_response import (
        OpenAILLMEvaluationsIntegrationDataflowsResponse,
    )
    from datadog_api_client.v2.model.open_aillm_evaluations_integration_account_settings_response import (
        OpenAILLMEvaluationsIntegrationAccountSettingsResponse,
    )
    from datadog_api_client.v2.model.open_aillm_evaluations_integration_account_bearer_token_auth_response import (
        OpenAILLMEvaluationsIntegrationAccountBearerTokenAuthResponse,
    )


class OpenAILLMEvaluationsIntegrationAccountResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.open_aillm_evaluations_integration_account_authentication_response import (
            OpenAILLMEvaluationsIntegrationAccountAuthenticationResponse,
        )
        from datadog_api_client.v2.model.open_aillm_evaluations_integration_dataflows_response import (
            OpenAILLMEvaluationsIntegrationDataflowsResponse,
        )
        from datadog_api_client.v2.model.open_aillm_evaluations_integration_account_settings_response import (
            OpenAILLMEvaluationsIntegrationAccountSettingsResponse,
        )

        return {
            "authentication": (OpenAILLMEvaluationsIntegrationAccountAuthenticationResponse,),
            "dataflows": (OpenAILLMEvaluationsIntegrationDataflowsResponse,),
            "name": (str,),
            "settings": (OpenAILLMEvaluationsIntegrationAccountSettingsResponse,),
        }

    attribute_map = {
        "authentication": "authentication",
        "dataflows": "dataflows",
        "name": "name",
        "settings": "settings",
    }

    def __init__(
        self_,
        name: str,
        settings: OpenAILLMEvaluationsIntegrationAccountSettingsResponse,
        authentication: Union[
            OpenAILLMEvaluationsIntegrationAccountAuthenticationResponse,
            OpenAILLMEvaluationsIntegrationAccountBearerTokenAuthResponse,
            UnsetType,
        ] = unset,
        dataflows: Union[OpenAILLMEvaluationsIntegrationDataflowsResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an OpenAI LLM Evaluations integration account returned in responses.

        :param authentication: Authentication configured on the OpenAI LLM Evaluations integration account.
        :type authentication: OpenAILLMEvaluationsIntegrationAccountAuthenticationResponse, optional

        :param dataflows: Data Datadog collects from OpenAI LLM Evaluations, keyed by dataflow ID.
        :type dataflows: OpenAILLMEvaluationsIntegrationDataflowsResponse, optional

        :param name: Human-readable name of the OpenAI LLM Evaluations integration account.
        :type name: str

        :param settings: Settings configured on the OpenAI LLM Evaluations integration account.
        :type settings: OpenAILLMEvaluationsIntegrationAccountSettingsResponse
        """
        if authentication is not unset:
            kwargs["authentication"] = authentication
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        super().__init__(kwargs)

        self_.name = name
        self_.settings = settings
