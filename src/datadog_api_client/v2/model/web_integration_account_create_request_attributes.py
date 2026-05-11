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
    from datadog_api_client.v2.model.web_integration_account_secrets import WebIntegrationAccountSecrets
    from datadog_api_client.v2.model.web_integration_account_settings import WebIntegrationAccountSettings


class WebIntegrationAccountCreateRequestAttributes(ModelNormal):
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
        self_, name: str, secrets: WebIntegrationAccountSecrets, settings: WebIntegrationAccountSettings, **kwargs
    ):
        """
        Attributes object for creating a web integration account.

        :param name: A human-readable name for the account. Must be unique among accounts of the same integration.
        :type name: str

        :param secrets: Integration-specific secrets. The shape of this object varies by integration. Secrets
            are write-only and never returned by the API.
        :type secrets: WebIntegrationAccountSecrets

        :param settings: Integration-specific settings. The shape of this object varies by integration.
        :type settings: WebIntegrationAccountSettings
        """
        super().__init__(kwargs)

        self_.name = name
        self_.secrets = secrets
        self_.settings = settings
