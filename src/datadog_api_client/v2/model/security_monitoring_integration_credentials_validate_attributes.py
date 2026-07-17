# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class SecurityMonitoringIntegrationCredentialsValidateAttributes(ModelComposed):
    def __init__(self, **kwargs):
        """
        The credentials to validate against the external entity source.

        :param domain: The domain associated with the external entity source.
        :type domain: str

        :param integration_type: The source type for a Google Workspace entity context sync.
        :type integration_type: SecurityMonitoringIntegrationTypeGoogleWorkspace

        :param secrets: Credentials for a Google Workspace entity context sync.
        :type secrets: SecurityMonitoringIntegrationConfigGoogleWorkspaceSecrets
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
        from datadog_api_client.v2.model.security_monitoring_google_workspace_integration_credentials_validate_attributes import (
            SecurityMonitoringGoogleWorkspaceIntegrationCredentialsValidateAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_okta_integration_credentials_validate_attributes import (
            SecurityMonitoringOktaIntegrationCredentialsValidateAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_entra_id_integration_credentials_validate_attributes import (
            SecurityMonitoringEntraIdIntegrationCredentialsValidateAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_crowd_strike_integration_credentials_validate_attributes import (
            SecurityMonitoringCrowdStrikeIntegrationCredentialsValidateAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_sentinel_one_integration_credentials_validate_attributes import (
            SecurityMonitoringSentinelOneIntegrationCredentialsValidateAttributes,
        )

        return {
            "oneOf": [
                SecurityMonitoringGoogleWorkspaceIntegrationCredentialsValidateAttributes,
                SecurityMonitoringOktaIntegrationCredentialsValidateAttributes,
                SecurityMonitoringEntraIdIntegrationCredentialsValidateAttributes,
                SecurityMonitoringCrowdStrikeIntegrationCredentialsValidateAttributes,
                SecurityMonitoringSentinelOneIntegrationCredentialsValidateAttributes,
            ],
        }
