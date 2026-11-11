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
    from datadog_api_client.v2.model.chat_gpt_enterprise_integration_account_authentication_update import (
        ChatGPTEnterpriseIntegrationAccountAuthenticationUpdate,
    )
    from datadog_api_client.v2.model.chat_gpt_enterprise_integration_dataflows_request import (
        ChatGPTEnterpriseIntegrationDataflowsRequest,
    )
    from datadog_api_client.v2.model.chat_gpt_enterprise_integration_account_settings_update import (
        ChatGPTEnterpriseIntegrationAccountSettingsUpdate,
    )
    from datadog_api_client.v2.model.chat_gpt_enterprise_integration_account_bearer_token_auth_update import (
        ChatGPTEnterpriseIntegrationAccountBearerTokenAuthUpdate,
    )


class ChatGPTEnterpriseIntegrationAccountUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.chat_gpt_enterprise_integration_account_authentication_update import (
            ChatGPTEnterpriseIntegrationAccountAuthenticationUpdate,
        )
        from datadog_api_client.v2.model.chat_gpt_enterprise_integration_dataflows_request import (
            ChatGPTEnterpriseIntegrationDataflowsRequest,
        )
        from datadog_api_client.v2.model.chat_gpt_enterprise_integration_account_settings_update import (
            ChatGPTEnterpriseIntegrationAccountSettingsUpdate,
        )

        return {
            "authentication": (ChatGPTEnterpriseIntegrationAccountAuthenticationUpdate,),
            "dataflows": (ChatGPTEnterpriseIntegrationDataflowsRequest,),
            "name": (str,),
            "settings": (ChatGPTEnterpriseIntegrationAccountSettingsUpdate,),
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
            ChatGPTEnterpriseIntegrationAccountAuthenticationUpdate,
            ChatGPTEnterpriseIntegrationAccountBearerTokenAuthUpdate,
            UnsetType,
        ] = unset,
        dataflows: Union[ChatGPTEnterpriseIntegrationDataflowsRequest, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        settings: Union[ChatGPTEnterpriseIntegrationAccountSettingsUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        Writable attributes used to update a ChatGPT Enterprise integration account. Every field is optional; only the fields provided are changed. When ``dataflows`` is provided, only the dataflow ids included in the request are modified; dataflows omitted from the map keep their current configuration.

        :param authentication: Authentication for updating the ChatGPT Enterprise integration account. Exactly one method is set.
        :type authentication: ChatGPTEnterpriseIntegrationAccountAuthenticationUpdate, optional

        :param dataflows: Data Datadog collects from ChatGPT Enterprise, keyed by dataflow id. Each dataflow turns on a distinct kind of collection: set ``enabled`` to start or stop it. Defaults listed on each dataflow apply when the account is created; on update, omitted fields keep their current values. Every dataflow requires a ChatGPT Enterprise workspace with access to the OpenAI Costs API; a dataflow enabled without it is stored but collects no data.
        :type dataflows: ChatGPTEnterpriseIntegrationDataflowsRequest, optional

        :param name: Human-readable name of the ChatGPT Enterprise integration account.
        :type name: str, optional

        :param settings: Settings for updating the ChatGPT Enterprise integration account. Only the fields provided are changed.
        :type settings: ChatGPTEnterpriseIntegrationAccountSettingsUpdate, optional
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
