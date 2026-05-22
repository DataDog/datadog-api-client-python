# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_integration_type import SecurityMonitoringIntegrationType
    from datadog_api_client.v2.model.security_monitoring_integration_config_settings import (
        SecurityMonitoringIntegrationConfigSettings,
    )
    from datadog_api_client.v2.model.security_monitoring_integration_config_state import (
        SecurityMonitoringIntegrationConfigState,
    )


class SecurityMonitoringIntegrationConfigAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_integration_type import SecurityMonitoringIntegrationType
        from datadog_api_client.v2.model.security_monitoring_integration_config_settings import (
            SecurityMonitoringIntegrationConfigSettings,
        )
        from datadog_api_client.v2.model.security_monitoring_integration_config_state import (
            SecurityMonitoringIntegrationConfigState,
        )

        return {
            "created_at": (datetime,),
            "domain": (str,),
            "enabled": (bool,),
            "integration_type": (SecurityMonitoringIntegrationType,),
            "modified_at": (datetime,),
            "name": (str,),
            "settings": (SecurityMonitoringIntegrationConfigSettings,),
            "state": (SecurityMonitoringIntegrationConfigState,),
        }

    attribute_map = {
        "created_at": "created_at",
        "domain": "domain",
        "enabled": "enabled",
        "integration_type": "integration_type",
        "modified_at": "modified_at",
        "name": "name",
        "settings": "settings",
        "state": "state",
    }

    def __init__(
        self_,
        domain: str,
        enabled: bool,
        integration_type: SecurityMonitoringIntegrationType,
        created_at: Union[datetime, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        settings: Union[SecurityMonitoringIntegrationConfigSettings, UnsetType] = unset,
        state: Union[SecurityMonitoringIntegrationConfigState, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of an entity context sync configuration as returned by the API.

        :param created_at: The time at which the entity context sync configuration was created.
        :type created_at: datetime, optional

        :param domain: The domain associated with the external entity source (for example, the customer's identity provider domain).
        :type domain: str

        :param enabled: Whether the sync is enabled and actively ingesting entities into Cloud SIEM.
        :type enabled: bool

        :param integration_type: The type of external source that provides entities to Cloud SIEM.
        :type integration_type: SecurityMonitoringIntegrationType

        :param modified_at: The time at which the entity context sync configuration was last modified.
        :type modified_at: datetime, optional

        :param name: The display name of the entity context sync configuration.
        :type name: str, optional

        :param settings: Free-form, non-sensitive settings for the entity context sync. The accepted keys depend on the source type.
        :type settings: SecurityMonitoringIntegrationConfigSettings, optional

        :param state: The state of the credentials configured on the entity context sync.
        :type state: SecurityMonitoringIntegrationConfigState, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if name is not unset:
            kwargs["name"] = name
        if settings is not unset:
            kwargs["settings"] = settings
        if state is not unset:
            kwargs["state"] = state
        super().__init__(kwargs)

        self_.domain = domain
        self_.enabled = enabled
        self_.integration_type = integration_type
