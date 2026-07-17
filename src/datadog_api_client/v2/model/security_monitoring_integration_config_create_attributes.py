# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class SecurityMonitoringIntegrationConfigCreateAttributes(ModelComposed):
    def __init__(self, **kwargs):
        """
        The attributes of the entity context sync configuration to create.

        :param domain: The domain associated with the external entity source.
        :type domain: str

        :param integration_type: The source type for a Google Workspace entity context sync.
        :type integration_type: SecurityMonitoringIntegrationTypeGoogleWorkspace

        :param name: The display name for the entity context sync configuration.
        :type name: str

        :param secrets: Credentials for a Google Workspace entity context sync.
        :type secrets: SecurityMonitoringIntegrationConfigGoogleWorkspaceSecrets

        :param settings: Free-form, non-sensitive settings for the entity context sync. The accepted keys depend on the source type.
        :type settings: SecurityMonitoringIntegrationConfigSettings, optional
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.security_monitoring_google_workspace_integration_config_create_attributes import (
            SecurityMonitoringGoogleWorkspaceIntegrationConfigCreateAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_okta_integration_config_create_attributes import (
            SecurityMonitoringOktaIntegrationConfigCreateAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_entra_id_integration_config_create_attributes import (
            SecurityMonitoringEntraIdIntegrationConfigCreateAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_crowd_strike_integration_config_create_attributes import (
            SecurityMonitoringCrowdStrikeIntegrationConfigCreateAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_sentinel_one_integration_config_create_attributes import (
            SecurityMonitoringSentinelOneIntegrationConfigCreateAttributes,
        )

        return {
            "oneOf": [
                SecurityMonitoringGoogleWorkspaceIntegrationConfigCreateAttributes,
                SecurityMonitoringOktaIntegrationConfigCreateAttributes,
                SecurityMonitoringEntraIdIntegrationConfigCreateAttributes,
                SecurityMonitoringCrowdStrikeIntegrationConfigCreateAttributes,
                SecurityMonitoringSentinelOneIntegrationConfigCreateAttributes,
            ],
        }
