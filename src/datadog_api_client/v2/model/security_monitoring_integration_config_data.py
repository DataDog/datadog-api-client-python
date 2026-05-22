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
    from datadog_api_client.v2.model.security_monitoring_integration_config_attributes import (
        SecurityMonitoringIntegrationConfigAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_integration_config_resource_type import (
        SecurityMonitoringIntegrationConfigResourceType,
    )


class SecurityMonitoringIntegrationConfigData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_integration_config_attributes import (
            SecurityMonitoringIntegrationConfigAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_integration_config_resource_type import (
            SecurityMonitoringIntegrationConfigResourceType,
        )

        return {
            "attributes": (SecurityMonitoringIntegrationConfigAttributes,),
            "id": (str,),
            "type": (SecurityMonitoringIntegrationConfigResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringIntegrationConfigAttributes,
        id: str,
        type: SecurityMonitoringIntegrationConfigResourceType,
        **kwargs,
    ):
        """
        An entity context sync configuration.

        :param attributes: The attributes of an entity context sync configuration as returned by the API.
        :type attributes: SecurityMonitoringIntegrationConfigAttributes

        :param id: The unique identifier of the integration configuration.
        :type id: str

        :param type: The type of the resource. The value should always be ``integration_config``.
        :type type: SecurityMonitoringIntegrationConfigResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
