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
    from datadog_api_client.v2.model.security_monitoring_integration_type_crowd_strike import (
        SecurityMonitoringIntegrationTypeCrowdStrike,
    )
    from datadog_api_client.v2.model.security_monitoring_integration_config_crowd_strike_secrets import (
        SecurityMonitoringIntegrationConfigCrowdStrikeSecrets,
    )


class SecurityMonitoringCrowdStrikeIntegrationCredentialsValidateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_integration_type_crowd_strike import (
            SecurityMonitoringIntegrationTypeCrowdStrike,
        )
        from datadog_api_client.v2.model.security_monitoring_integration_config_crowd_strike_secrets import (
            SecurityMonitoringIntegrationConfigCrowdStrikeSecrets,
        )

        return {
            "domain": (str,),
            "integration_type": (SecurityMonitoringIntegrationTypeCrowdStrike,),
            "secrets": (SecurityMonitoringIntegrationConfigCrowdStrikeSecrets,),
        }

    attribute_map = {
        "domain": "domain",
        "integration_type": "integration_type",
        "secrets": "secrets",
    }

    def __init__(
        self_,
        domain: str,
        integration_type: SecurityMonitoringIntegrationTypeCrowdStrike,
        secrets: SecurityMonitoringIntegrationConfigCrowdStrikeSecrets,
        **kwargs,
    ):
        """
        The CrowdStrike credentials to validate against the external entity source.

        :param domain: The domain associated with the external entity source.
        :type domain: str

        :param integration_type: The source type for a CrowdStrike entity context sync.
        :type integration_type: SecurityMonitoringIntegrationTypeCrowdStrike

        :param secrets: Credentials for a CrowdStrike entity context sync.
        :type secrets: SecurityMonitoringIntegrationConfigCrowdStrikeSecrets
        """
        super().__init__(kwargs)

        self_.domain = domain
        self_.integration_type = integration_type
        self_.secrets = secrets
