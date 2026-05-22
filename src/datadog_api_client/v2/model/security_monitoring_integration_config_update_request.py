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
    from datadog_api_client.v2.model.security_monitoring_integration_config_update_data import (
        SecurityMonitoringIntegrationConfigUpdateData,
    )


class SecurityMonitoringIntegrationConfigUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_integration_config_update_data import (
            SecurityMonitoringIntegrationConfigUpdateData,
        )

        return {
            "data": (SecurityMonitoringIntegrationConfigUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SecurityMonitoringIntegrationConfigUpdateData, **kwargs):
        """
        Request body to update an entity context sync configuration. Supports partial updates.

        :param data: The entity context sync configuration fields to update.
        :type data: SecurityMonitoringIntegrationConfigUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
