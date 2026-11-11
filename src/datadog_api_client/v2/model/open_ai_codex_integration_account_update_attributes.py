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
    from datadog_api_client.v2.model.open_ai_codex_integration_account_authentication_update import (
        OpenAICodexIntegrationAccountAuthenticationUpdate,
    )
    from datadog_api_client.v2.model.open_ai_codex_integration_dataflows_request import (
        OpenAICodexIntegrationDataflowsRequest,
    )
    from datadog_api_client.v2.model.open_ai_codex_integration_account_settings_update import (
        OpenAICodexIntegrationAccountSettingsUpdate,
    )
    from datadog_api_client.v2.model.open_ai_codex_integration_account_bearer_token_auth_update import (
        OpenAICodexIntegrationAccountBearerTokenAuthUpdate,
    )


class OpenAICodexIntegrationAccountUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.open_ai_codex_integration_account_authentication_update import (
            OpenAICodexIntegrationAccountAuthenticationUpdate,
        )
        from datadog_api_client.v2.model.open_ai_codex_integration_dataflows_request import (
            OpenAICodexIntegrationDataflowsRequest,
        )
        from datadog_api_client.v2.model.open_ai_codex_integration_account_settings_update import (
            OpenAICodexIntegrationAccountSettingsUpdate,
        )

        return {
            "authentication": (OpenAICodexIntegrationAccountAuthenticationUpdate,),
            "dataflows": (OpenAICodexIntegrationDataflowsRequest,),
            "name": (str,),
            "settings": (OpenAICodexIntegrationAccountSettingsUpdate,),
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
            OpenAICodexIntegrationAccountAuthenticationUpdate,
            OpenAICodexIntegrationAccountBearerTokenAuthUpdate,
            UnsetType,
        ] = unset,
        dataflows: Union[OpenAICodexIntegrationDataflowsRequest, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        settings: Union[OpenAICodexIntegrationAccountSettingsUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        Writable attributes used to update an OpenAI Codex integration account. Every field is optional; only the fields provided are changed. When ``dataflows`` is provided, only the dataflow ids included in the request are modified; dataflows omitted from the map keep their current configuration.

        :param authentication: Authentication for updating the OpenAI Codex integration account. Exactly one method is set.
        :type authentication: OpenAICodexIntegrationAccountAuthenticationUpdate, optional

        :param dataflows: Data Datadog collects from OpenAI Codex, keyed by dataflow id. Daily Codex analytics metrics are always collected; each dataflow here adds a further kind of collection on top of that baseline, so set ``enabled`` to start or stop it. Defaults listed on each dataflow apply when the account is created; on update, omitted fields keep their current values. Every dataflow requires an OpenAI enterprise subscription with Codex enabled; a dataflow enabled without it is stored but collects no data.
        :type dataflows: OpenAICodexIntegrationDataflowsRequest, optional

        :param name: Human-readable name of the OpenAI Codex integration account.
        :type name: str, optional

        :param settings: Settings for updating the OpenAI Codex integration account. Only the fields provided are changed.
        :type settings: OpenAICodexIntegrationAccountSettingsUpdate, optional
        """
        if authentication is not unset:
            kwargs["authentication"] = authentication
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        if name is not unset:
            kwargs["name"] = name
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)
