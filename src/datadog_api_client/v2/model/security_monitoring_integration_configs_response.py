# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_integration_config_data import (
        SecurityMonitoringIntegrationConfigData,
    )


class SecurityMonitoringIntegrationConfigsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_integration_config_data import (
            SecurityMonitoringIntegrationConfigData,
        )

        return {
            "data": ([SecurityMonitoringIntegrationConfigData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[SecurityMonitoringIntegrationConfigData], **kwargs):
        """
        Response containing a list of entity context sync configurations.

        :param data: The list of integration configurations.
        :type data: [SecurityMonitoringIntegrationConfigData]
        """
        super().__init__(kwargs)

        self_.data = data
