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
    from datadog_api_client.v2.model.security_monitoring_integration_type_entra_id import (
        SecurityMonitoringIntegrationTypeEntraId,
    )
    from datadog_api_client.v2.model.security_monitoring_integration_config_settings import (
        SecurityMonitoringIntegrationConfigSettings,
    )


class SecurityMonitoringEntraIdIntegrationConfigCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_integration_type_entra_id import (
            SecurityMonitoringIntegrationTypeEntraId,
        )
        from datadog_api_client.v2.model.security_monitoring_integration_config_settings import (
            SecurityMonitoringIntegrationConfigSettings,
        )

        return {
            "domain": (str,),
            "integration_type": (SecurityMonitoringIntegrationTypeEntraId,),
            "name": (str,),
            "settings": (SecurityMonitoringIntegrationConfigSettings,),
        }

    attribute_map = {
        "domain": "domain",
        "integration_type": "integration_type",
        "name": "name",
        "settings": "settings",
    }

    def __init__(
        self_,
        domain: str,
        integration_type: SecurityMonitoringIntegrationTypeEntraId,
        name: str,
        settings: Union[SecurityMonitoringIntegrationConfigSettings, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of an Entra ID entity context sync configuration to create.

        :param domain: The domain associated with the external entity source.
        :type domain: str

        :param integration_type: The source type for an Entra ID entity context sync.
        :type integration_type: SecurityMonitoringIntegrationTypeEntraId

        :param name: The display name for the entity context sync configuration.
        :type name: str

        :param settings: Free-form, non-sensitive settings for the entity context sync. The accepted keys depend on the source type.
        :type settings: SecurityMonitoringIntegrationConfigSettings, optional
        """
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)

        self_.domain = domain
        self_.integration_type = integration_type
        self_.name = name
