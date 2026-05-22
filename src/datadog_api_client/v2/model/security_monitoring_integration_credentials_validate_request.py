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
    from datadog_api_client.v2.model.security_monitoring_integration_credentials_validate_data import (
        SecurityMonitoringIntegrationCredentialsValidateData,
    )


class SecurityMonitoringIntegrationCredentialsValidateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_integration_credentials_validate_data import (
            SecurityMonitoringIntegrationCredentialsValidateData,
        )

        return {
            "data": (SecurityMonitoringIntegrationCredentialsValidateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SecurityMonitoringIntegrationCredentialsValidateData, **kwargs):
        """
        Request body to validate credentials against an external entity source before creating a sync configuration.

        :param data: The credentials to validate.
        :type data: SecurityMonitoringIntegrationCredentialsValidateData
        """
        super().__init__(kwargs)

        self_.data = data
