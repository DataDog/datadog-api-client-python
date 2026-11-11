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
    from datadog_api_client.v2.model.open_ai_codex_integration_account_authentication_request import (
        OpenAICodexIntegrationAccountAuthenticationRequest,
    )
    from datadog_api_client.v2.model.open_ai_codex_integration_dataflows_request import (
        OpenAICodexIntegrationDataflowsRequest,
    )
    from datadog_api_client.v2.model.open_ai_codex_integration_account_settings_request import (
        OpenAICodexIntegrationAccountSettingsRequest,
    )
    from datadog_api_client.v2.model.open_ai_codex_integration_account_bearer_token_auth_request import (
        OpenAICodexIntegrationAccountBearerTokenAuthRequest,
    )


class OpenAICodexIntegrationAccountCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.open_ai_codex_integration_account_authentication_request import (
            OpenAICodexIntegrationAccountAuthenticationRequest,
        )
        from datadog_api_client.v2.model.open_ai_codex_integration_dataflows_request import (
            OpenAICodexIntegrationDataflowsRequest,
        )
        from datadog_api_client.v2.model.open_ai_codex_integration_account_settings_request import (
            OpenAICodexIntegrationAccountSettingsRequest,
        )

        return {
            "authentication": (OpenAICodexIntegrationAccountAuthenticationRequest,),
            "dataflows": (OpenAICodexIntegrationDataflowsRequest,),
            "name": (str,),
            "settings": (OpenAICodexIntegrationAccountSettingsRequest,),
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
            OpenAICodexIntegrationAccountAuthenticationRequest, OpenAICodexIntegrationAccountBearerTokenAuthRequest
        ],
        name: str,
        settings: OpenAICodexIntegrationAccountSettingsRequest,
        dataflows: Union[OpenAICodexIntegrationDataflowsRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Writable attributes used to create an OpenAI Codex integration account.

        :param authentication: Authentication for creating the OpenAI Codex integration account. Exactly one method is set.
        :type authentication: OpenAICodexIntegrationAccountAuthenticationRequest

        :param dataflows: Data Datadog collects from OpenAI Codex, keyed by dataflow id. Daily Codex analytics metrics are always collected; each dataflow here adds a further kind of collection on top of that baseline, so set ``enabled`` to start or stop it. Defaults listed on each dataflow apply when the account is created; on update, omitted fields keep their current values. Every dataflow requires an OpenAI enterprise subscription with Codex enabled; a dataflow enabled without it is stored but collects no data.
        :type dataflows: OpenAICodexIntegrationDataflowsRequest, optional

        :param name: Human-readable name of the OpenAI Codex integration account.
        :type name: str

        :param settings: Settings for creating the OpenAI Codex integration account.
        :type settings: OpenAICodexIntegrationAccountSettingsRequest
        """
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        super().__init__(kwargs)

        self_.authentication = authentication
        self_.name = name
        self_.settings = settings
