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


class SecurityMonitoringIntegrationCredentialsValidateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_integration_type import SecurityMonitoringIntegrationType
        from datadog_api_client.v2.model.security_monitoring_integration_config_secrets import (
            SecurityMonitoringIntegrationConfigSecrets,
        )

        return {
            "domain": (str,),
            "integration_type": (SecurityMonitoringIntegrationType,),
            "secrets": (SecurityMonitoringIntegrationConfigSecrets,),
        }

    attribute_map = {
        "domain": "domain",
        "integration_type": "integration_type",
        "secrets": "secrets",
    }

    def __init__(
        self_,
        domain: str,
        integration_type: SecurityMonitoringIntegrationType,
        secrets: Union[SecurityMonitoringIntegrationConfigSecrets, UnsetType] = unset,
        **kwargs,
    ):
        """
        The credentials to validate against the external entity source.

        :param domain: The domain associated with the external entity source.
        :type domain: str

        :param integration_type: The type of external source that provides entities to Cloud SIEM.
        :type integration_type: SecurityMonitoringIntegrationType

        :param secrets: The secrets used to authenticate against the external entity source. The accepted keys depend on the source type
            (for example, ``admin_email`` for Google Workspace). Not required for source types that do not use secrets (for example, ``ENTRA_ID`` ).
        :type secrets: SecurityMonitoringIntegrationConfigSecrets, optional
        """
        if secrets is not unset:
            kwargs["secrets"] = secrets
        super().__init__(kwargs)

        self_.domain = domain
        self_.integration_type = integration_type
