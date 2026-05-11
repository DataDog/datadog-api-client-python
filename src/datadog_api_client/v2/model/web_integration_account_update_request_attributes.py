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
    from datadog_api_client.v2.model.web_integration_account_secrets import WebIntegrationAccountSecrets
    from datadog_api_client.v2.model.web_integration_account_settings import WebIntegrationAccountSettings


class WebIntegrationAccountUpdateRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.web_integration_account_secrets import WebIntegrationAccountSecrets
        from datadog_api_client.v2.model.web_integration_account_settings import WebIntegrationAccountSettings

        return {
            "name": (str,),
            "secrets": (WebIntegrationAccountSecrets,),
            "settings": (WebIntegrationAccountSettings,),
        }

    attribute_map = {
        "name": "name",
        "secrets": "secrets",
        "settings": "settings",
    }

    def __init__(
        self_,
        name: Union[str, UnsetType] = unset,
        secrets: Union[WebIntegrationAccountSecrets, UnsetType] = unset,
        settings: Union[WebIntegrationAccountSettings, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes object for updating a web integration account.

        :param name: A human-readable name for the account.
        :type name: str, optional

        :param secrets: Integration-specific secrets. The shape of this object varies by integration. Secrets
            are write-only and never returned by the API.
        :type secrets: WebIntegrationAccountSecrets, optional

        :param settings: Integration-specific settings. The shape of this object varies by integration.
        :type settings: WebIntegrationAccountSettings, optional
        """
        if name is not unset:
            kwargs["name"] = name
        if secrets is not unset:
            kwargs["secrets"] = secrets
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)
