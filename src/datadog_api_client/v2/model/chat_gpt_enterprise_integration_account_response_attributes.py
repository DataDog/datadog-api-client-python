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
    from datadog_api_client.v2.model.chat_gpt_enterprise_integration_account_authentication_response import (
        ChatGPTEnterpriseIntegrationAccountAuthenticationResponse,
    )
    from datadog_api_client.v2.model.chat_gpt_enterprise_integration_dataflows_response import (
        ChatGPTEnterpriseIntegrationDataflowsResponse,
    )
    from datadog_api_client.v2.model.chat_gpt_enterprise_integration_account_settings_response import (
        ChatGPTEnterpriseIntegrationAccountSettingsResponse,
    )
    from datadog_api_client.v2.model.chat_gpt_enterprise_integration_account_bearer_token_auth_response import (
        ChatGPTEnterpriseIntegrationAccountBearerTokenAuthResponse,
    )


class ChatGPTEnterpriseIntegrationAccountResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.chat_gpt_enterprise_integration_account_authentication_response import (
            ChatGPTEnterpriseIntegrationAccountAuthenticationResponse,
        )
        from datadog_api_client.v2.model.chat_gpt_enterprise_integration_dataflows_response import (
            ChatGPTEnterpriseIntegrationDataflowsResponse,
        )
        from datadog_api_client.v2.model.chat_gpt_enterprise_integration_account_settings_response import (
            ChatGPTEnterpriseIntegrationAccountSettingsResponse,
        )

        return {
            "authentication": (ChatGPTEnterpriseIntegrationAccountAuthenticationResponse,),
            "dataflows": (ChatGPTEnterpriseIntegrationDataflowsResponse,),
            "name": (str,),
            "settings": (ChatGPTEnterpriseIntegrationAccountSettingsResponse,),
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
        settings: ChatGPTEnterpriseIntegrationAccountSettingsResponse,
        authentication: Union[
            ChatGPTEnterpriseIntegrationAccountAuthenticationResponse,
            ChatGPTEnterpriseIntegrationAccountBearerTokenAuthResponse,
            UnsetType,
        ] = unset,
        dataflows: Union[ChatGPTEnterpriseIntegrationDataflowsResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a ChatGPT Enterprise integration account returned in responses.

        :param authentication: Authentication configured on the ChatGPT Enterprise integration account.
        :type authentication: ChatGPTEnterpriseIntegrationAccountAuthenticationResponse, optional

        :param dataflows: Data Datadog collects from ChatGPT Enterprise, keyed by dataflow id.
        :type dataflows: ChatGPTEnterpriseIntegrationDataflowsResponse, optional

        :param name: Human-readable name of the ChatGPT Enterprise integration account.
        :type name: str

        :param settings: Settings configured on the ChatGPT Enterprise integration account.
        :type settings: ChatGPTEnterpriseIntegrationAccountSettingsResponse
        """
        if authentication is not unset:
            kwargs["authentication"] = authentication
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        super().__init__(kwargs)

        self_.name = name
        self_.settings = settings
