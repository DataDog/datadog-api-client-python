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
    from datadog_api_client.v2.model.security_monitoring_integration_config_update_attributes import (
        SecurityMonitoringIntegrationConfigUpdateAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_integration_config_resource_type import (
        SecurityMonitoringIntegrationConfigResourceType,
    )


class SecurityMonitoringIntegrationConfigUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_integration_config_update_attributes import (
            SecurityMonitoringIntegrationConfigUpdateAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_integration_config_resource_type import (
            SecurityMonitoringIntegrationConfigResourceType,
        )

        return {
            "attributes": (SecurityMonitoringIntegrationConfigUpdateAttributes,),
            "type": (SecurityMonitoringIntegrationConfigResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringIntegrationConfigUpdateAttributes,
        type: SecurityMonitoringIntegrationConfigResourceType,
        **kwargs,
    ):
        """
        The entity context sync configuration fields to update.

        :param attributes: Fields to update on the entity context sync configuration. All fields are optional.
        :type attributes: SecurityMonitoringIntegrationConfigUpdateAttributes

        :param type: The type of the resource. The value should always be ``integration_config``.
        :type type: SecurityMonitoringIntegrationConfigResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
