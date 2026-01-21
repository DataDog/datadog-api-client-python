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
    from datadog_api_client.v2.model.web_integration_account_schema_response_secrets_object import (
        WebIntegrationAccountSchemaResponseSecretsObject,
    )
    from datadog_api_client.v2.model.web_integration_account_schema_response_settings_object import (
        WebIntegrationAccountSchemaResponseSettingsObject,
    )


class WebIntegrationAccountSchemaResponseProperties(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.web_integration_account_schema_response_secrets_object import (
            WebIntegrationAccountSchemaResponseSecretsObject,
        )
        from datadog_api_client.v2.model.web_integration_account_schema_response_settings_object import (
            WebIntegrationAccountSchemaResponseSettingsObject,
        )

        return {
            "secrets": (WebIntegrationAccountSchemaResponseSecretsObject,),
            "settings": (WebIntegrationAccountSchemaResponseSettingsObject,),
        }

    attribute_map = {
        "secrets": "secrets",
        "settings": "settings",
    }

    def __init__(
        self_,
        secrets: WebIntegrationAccountSchemaResponseSecretsObject,
        settings: WebIntegrationAccountSchemaResponseSettingsObject,
        **kwargs,
    ):
        """
        The properties object containing settings and secrets schema definitions.
        Both are always present in every integration schema.

        :param secrets: JSON Schema definition for the secrets object.
            Contains sensitive credentials required for the integration such as API keys,
            tokens, and passwords. These values are write-only and never returned in responses.
        :type secrets: WebIntegrationAccountSchemaResponseSecretsObject

        :param settings: JSON Schema definition for the settings object.
            Contains integration-specific configuration fields such as account identifiers,
            feature toggles, and non-sensitive configuration options.
        :type settings: WebIntegrationAccountSchemaResponseSettingsObject
        """
        super().__init__(kwargs)

        self_.secrets = secrets
        self_.settings = settings
