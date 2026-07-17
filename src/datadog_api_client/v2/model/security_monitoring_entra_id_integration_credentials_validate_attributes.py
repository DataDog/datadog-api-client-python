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
    from datadog_api_client.v2.model.security_monitoring_integration_type_entra_id import (
        SecurityMonitoringIntegrationTypeEntraId,
    )


class SecurityMonitoringEntraIdIntegrationCredentialsValidateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_integration_type_entra_id import (
            SecurityMonitoringIntegrationTypeEntraId,
        )

        return {
            "domain": (str,),
            "integration_type": (SecurityMonitoringIntegrationTypeEntraId,),
        }

    attribute_map = {
        "domain": "domain",
        "integration_type": "integration_type",
    }

    def __init__(self_, domain: str, integration_type: SecurityMonitoringIntegrationTypeEntraId, **kwargs):
        """
        The Entra ID credentials to validate against the external entity source.

        :param domain: The domain associated with the external entity source.
        :type domain: str

        :param integration_type: The source type for an Entra ID entity context sync.
        :type integration_type: SecurityMonitoringIntegrationTypeEntraId
        """
        super().__init__(kwargs)

        self_.domain = domain
        self_.integration_type = integration_type
