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
    from datadog_api_client.v2.model.chat_gpt_enterprise_integration_account_authentication_request import (
        ChatGPTEnterpriseIntegrationAccountAuthenticationRequest,
    )
    from datadog_api_client.v2.model.chat_gpt_enterprise_integration_dataflows_request import (
        ChatGPTEnterpriseIntegrationDataflowsRequest,
    )
    from datadog_api_client.v2.model.chat_gpt_enterprise_integration_account_settings_request import (
        ChatGPTEnterpriseIntegrationAccountSettingsRequest,
    )
    from datadog_api_client.v2.model.chat_gpt_enterprise_integration_account_bearer_token_auth_request import (
        ChatGPTEnterpriseIntegrationAccountBearerTokenAuthRequest,
    )


class ChatGPTEnterpriseIntegrationAccountCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.chat_gpt_enterprise_integration_account_authentication_request import (
            ChatGPTEnterpriseIntegrationAccountAuthenticationRequest,
        )
        from datadog_api_client.v2.model.chat_gpt_enterprise_integration_dataflows_request import (
            ChatGPTEnterpriseIntegrationDataflowsRequest,
        )
        from datadog_api_client.v2.model.chat_gpt_enterprise_integration_account_settings_request import (
            ChatGPTEnterpriseIntegrationAccountSettingsRequest,
        )

        return {
            "authentication": (ChatGPTEnterpriseIntegrationAccountAuthenticationRequest,),
            "dataflows": (ChatGPTEnterpriseIntegrationDataflowsRequest,),
            "name": (str,),
            "settings": (ChatGPTEnterpriseIntegrationAccountSettingsRequest,),
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
            ChatGPTEnterpriseIntegrationAccountAuthenticationRequest,
            ChatGPTEnterpriseIntegrationAccountBearerTokenAuthRequest,
        ],
        name: str,
        settings: ChatGPTEnterpriseIntegrationAccountSettingsRequest,
        dataflows: Union[ChatGPTEnterpriseIntegrationDataflowsRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Writable attributes used to create a ChatGPT Enterprise integration account.

        :param authentication: Authentication for creating the ChatGPT Enterprise integration account. Exactly one method is set.
        :type authentication: ChatGPTEnterpriseIntegrationAccountAuthenticationRequest

        :param dataflows: Data Datadog collects from ChatGPT Enterprise, keyed by dataflow ID. Each dataflow turns on a distinct type of collection. Set ``enabled`` to start or stop a dataflow. The default for each dataflow applies when the account is created. On update, omitted fields keep their current values. Every dataflow requires a ChatGPT Enterprise workspace with access to the OpenAI Costs API. If you enable a dataflow without this access, Datadog stores the setting but collects no data.
        :type dataflows: ChatGPTEnterpriseIntegrationDataflowsRequest, optional

        :param name: Human-readable name of the ChatGPT Enterprise integration account.
        :type name: str

        :param settings: Settings for creating the ChatGPT Enterprise integration account.
        :type settings: ChatGPTEnterpriseIntegrationAccountSettingsRequest
        """
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        super().__init__(kwargs)

        self_.authentication = authentication
        self_.name = name
        self_.settings = settings
