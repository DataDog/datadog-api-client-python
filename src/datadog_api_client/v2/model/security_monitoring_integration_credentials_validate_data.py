# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_integration_credentials_validate_attributes import (
        SecurityMonitoringIntegrationCredentialsValidateAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_integration_config_resource_type import (
        SecurityMonitoringIntegrationConfigResourceType,
    )
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


class SecurityMonitoringIntegrationCredentialsValidateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_integration_credentials_validate_attributes import (
            SecurityMonitoringIntegrationCredentialsValidateAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_integration_config_resource_type import (
            SecurityMonitoringIntegrationConfigResourceType,
        )

        return {
            "attributes": (SecurityMonitoringIntegrationCredentialsValidateAttributes,),
            "type": (SecurityMonitoringIntegrationConfigResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[
            SecurityMonitoringIntegrationCredentialsValidateAttributes,
            SecurityMonitoringGoogleWorkspaceIntegrationCredentialsValidateAttributes,
            SecurityMonitoringOktaIntegrationCredentialsValidateAttributes,
            SecurityMonitoringEntraIdIntegrationCredentialsValidateAttributes,
            SecurityMonitoringCrowdStrikeIntegrationCredentialsValidateAttributes,
            SecurityMonitoringSentinelOneIntegrationCredentialsValidateAttributes,
        ],
        type: SecurityMonitoringIntegrationConfigResourceType,
        **kwargs,
    ):
        """
        The credentials to validate.

        :param attributes: The credentials to validate against the external entity source.
        :type attributes: SecurityMonitoringIntegrationCredentialsValidateAttributes

        :param type: The type of the resource. The value should always be ``integration_config``.
        :type type: SecurityMonitoringIntegrationConfigResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
