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
    from datadog_api_client.v2.model.security_monitoring_integration_type import SecurityMonitoringIntegrationType
    from datadog_api_client.v2.model.security_monitoring_integration_config_secrets import (
        SecurityMonitoringIntegrationConfigSecrets,
    )
    from datadog_api_client.v2.model.security_monitoring_integration_config_settings import (
        SecurityMonitoringIntegrationConfigSettings,
    )


class SecurityMonitoringIntegrationConfigCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_integration_type import SecurityMonitoringIntegrationType
        from datadog_api_client.v2.model.security_monitoring_integration_config_secrets import (
            SecurityMonitoringIntegrationConfigSecrets,
        )
        from datadog_api_client.v2.model.security_monitoring_integration_config_settings import (
            SecurityMonitoringIntegrationConfigSettings,
        )

        return {
            "domain": (str,),
            "integration_type": (SecurityMonitoringIntegrationType,),
            "name": (str,),
            "secrets": (SecurityMonitoringIntegrationConfigSecrets,),
            "settings": (SecurityMonitoringIntegrationConfigSettings,),
        }

    attribute_map = {
        "domain": "domain",
        "integration_type": "integration_type",
        "name": "name",
        "secrets": "secrets",
        "settings": "settings",
    }

    def __init__(
        self_,
        domain: str,
        integration_type: SecurityMonitoringIntegrationType,
        name: str,
        secrets: Union[SecurityMonitoringIntegrationConfigSecrets, UnsetType] = unset,
        settings: Union[SecurityMonitoringIntegrationConfigSettings, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of the entity context sync configuration to create.

        :param domain: The domain associated with the external entity source.
        :type domain: str

        :param integration_type: The type of external source that provides entities to Cloud SIEM.
        :type integration_type: SecurityMonitoringIntegrationType

        :param name: The display name for the entity context sync configuration.
        :type name: str

        :param secrets: The secrets used to authenticate against the external entity source. The accepted keys depend on the source type
            (for example, ``admin_email`` for Google Workspace). Not required for source types that do not use secrets (for example, ``ENTRA_ID`` ).
        :type secrets: SecurityMonitoringIntegrationConfigSecrets, optional

        :param settings: Free-form, non-sensitive settings for the entity context sync. The accepted keys depend on the source type.
        :type settings: SecurityMonitoringIntegrationConfigSettings, optional
        """
        if secrets is not unset:
            kwargs["secrets"] = secrets
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)

        self_.domain = domain
        self_.integration_type = integration_type
        self_.name = name
