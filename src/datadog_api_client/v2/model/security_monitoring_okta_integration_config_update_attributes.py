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
    from datadog_api_client.v2.model.security_monitoring_integration_type_okta import (
        SecurityMonitoringIntegrationTypeOkta,
    )
    from datadog_api_client.v2.model.security_monitoring_integration_config_okta_secrets import (
        SecurityMonitoringIntegrationConfigOktaSecrets,
    )
    from datadog_api_client.v2.model.security_monitoring_integration_config_settings import (
        SecurityMonitoringIntegrationConfigSettings,
    )


class SecurityMonitoringOktaIntegrationConfigUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_integration_type_okta import (
            SecurityMonitoringIntegrationTypeOkta,
        )
        from datadog_api_client.v2.model.security_monitoring_integration_config_okta_secrets import (
            SecurityMonitoringIntegrationConfigOktaSecrets,
        )
        from datadog_api_client.v2.model.security_monitoring_integration_config_settings import (
            SecurityMonitoringIntegrationConfigSettings,
        )

        return {
            "domain": (str,),
            "enabled": (bool,),
            "integration_type": (SecurityMonitoringIntegrationTypeOkta,),
            "name": (str,),
            "secrets": (SecurityMonitoringIntegrationConfigOktaSecrets,),
            "settings": (SecurityMonitoringIntegrationConfigSettings,),
        }

    attribute_map = {
        "domain": "domain",
        "enabled": "enabled",
        "integration_type": "integration_type",
        "name": "name",
        "secrets": "secrets",
        "settings": "settings",
    }

    def __init__(
        self_,
        integration_type: SecurityMonitoringIntegrationTypeOkta,
        domain: Union[str, UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        secrets: Union[SecurityMonitoringIntegrationConfigOktaSecrets, UnsetType] = unset,
        settings: Union[SecurityMonitoringIntegrationConfigSettings, UnsetType] = unset,
        **kwargs,
    ):
        """
        Fields to update on an Okta entity context sync configuration.

        :param domain: The new domain associated with the external entity source.
        :type domain: str, optional

        :param enabled: Whether the entity context sync should be enabled.
        :type enabled: bool, optional

        :param integration_type: The source type for an Okta entity context sync.
        :type integration_type: SecurityMonitoringIntegrationTypeOkta

        :param name: The new display name for the entity context sync configuration.
        :type name: str, optional

        :param secrets: Credentials for an Okta entity context sync.
        :type secrets: SecurityMonitoringIntegrationConfigOktaSecrets, optional

        :param settings: Free-form, non-sensitive settings for the entity context sync. The accepted keys depend on the source type.
        :type settings: SecurityMonitoringIntegrationConfigSettings, optional
        """
        if domain is not unset:
            kwargs["domain"] = domain
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if name is not unset:
            kwargs["name"] = name
        if secrets is not unset:
            kwargs["secrets"] = secrets
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)

        self_.integration_type = integration_type
