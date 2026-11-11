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
    from datadog_api_client.v2.model.open_ai_codex_integration_account_authentication_response import (
        OpenAICodexIntegrationAccountAuthenticationResponse,
    )
    from datadog_api_client.v2.model.open_ai_codex_integration_dataflows_response import (
        OpenAICodexIntegrationDataflowsResponse,
    )
    from datadog_api_client.v2.model.open_ai_codex_integration_account_settings_response import (
        OpenAICodexIntegrationAccountSettingsResponse,
    )
    from datadog_api_client.v2.model.open_ai_codex_integration_account_bearer_token_auth_response import (
        OpenAICodexIntegrationAccountBearerTokenAuthResponse,
    )


class OpenAICodexIntegrationAccountResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.open_ai_codex_integration_account_authentication_response import (
            OpenAICodexIntegrationAccountAuthenticationResponse,
        )
        from datadog_api_client.v2.model.open_ai_codex_integration_dataflows_response import (
            OpenAICodexIntegrationDataflowsResponse,
        )
        from datadog_api_client.v2.model.open_ai_codex_integration_account_settings_response import (
            OpenAICodexIntegrationAccountSettingsResponse,
        )

        return {
            "authentication": (OpenAICodexIntegrationAccountAuthenticationResponse,),
            "dataflows": (OpenAICodexIntegrationDataflowsResponse,),
            "name": (str,),
            "settings": (OpenAICodexIntegrationAccountSettingsResponse,),
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
        settings: OpenAICodexIntegrationAccountSettingsResponse,
        authentication: Union[
            OpenAICodexIntegrationAccountAuthenticationResponse,
            OpenAICodexIntegrationAccountBearerTokenAuthResponse,
            UnsetType,
        ] = unset,
        dataflows: Union[OpenAICodexIntegrationDataflowsResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an OpenAI Codex integration account returned in responses.

        :param authentication: Authentication configured on the OpenAI Codex integration account.
        :type authentication: OpenAICodexIntegrationAccountAuthenticationResponse, optional

        :param dataflows: Data Datadog collects from OpenAI Codex, keyed by dataflow id.
        :type dataflows: OpenAICodexIntegrationDataflowsResponse, optional

        :param name: Human-readable name of the OpenAI Codex integration account.
        :type name: str

        :param settings: Settings configured on the OpenAI Codex integration account.
        :type settings: OpenAICodexIntegrationAccountSettingsResponse
        """
        if authentication is not unset:
            kwargs["authentication"] = authentication
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        super().__init__(kwargs)

        self_.name = name
        self_.settings = settings
