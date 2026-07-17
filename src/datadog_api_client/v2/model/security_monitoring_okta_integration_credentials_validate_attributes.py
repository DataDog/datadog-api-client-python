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
    from datadog_api_client.v2.model.security_monitoring_integration_type_okta import (
        SecurityMonitoringIntegrationTypeOkta,
    )
    from datadog_api_client.v2.model.security_monitoring_integration_config_okta_secrets import (
        SecurityMonitoringIntegrationConfigOktaSecrets,
    )


class SecurityMonitoringOktaIntegrationCredentialsValidateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_integration_type_okta import (
            SecurityMonitoringIntegrationTypeOkta,
        )
        from datadog_api_client.v2.model.security_monitoring_integration_config_okta_secrets import (
            SecurityMonitoringIntegrationConfigOktaSecrets,
        )

        return {
            "domain": (str,),
            "integration_type": (SecurityMonitoringIntegrationTypeOkta,),
            "secrets": (SecurityMonitoringIntegrationConfigOktaSecrets,),
        }

    attribute_map = {
        "domain": "domain",
        "integration_type": "integration_type",
        "secrets": "secrets",
    }

    def __init__(
        self_,
        domain: str,
        integration_type: SecurityMonitoringIntegrationTypeOkta,
        secrets: SecurityMonitoringIntegrationConfigOktaSecrets,
        **kwargs,
    ):
        """
        The Okta credentials to validate against the external entity source.

        :param domain: The domain associated with the external entity source.
        :type domain: str

        :param integration_type: The source type for an Okta entity context sync.
        :type integration_type: SecurityMonitoringIntegrationTypeOkta

        :param secrets: Credentials for an Okta entity context sync.
        :type secrets: SecurityMonitoringIntegrationConfigOktaSecrets
        """
        super().__init__(kwargs)

        self_.domain = domain
        self_.integration_type = integration_type
        self_.secrets = secrets
