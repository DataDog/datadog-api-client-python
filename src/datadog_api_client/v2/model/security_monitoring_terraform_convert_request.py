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
    from datadog_api_client.v2.model.security_monitoring_terraform_convert_data import (
        SecurityMonitoringTerraformConvertData,
    )


class SecurityMonitoringTerraformConvertRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_terraform_convert_data import (
            SecurityMonitoringTerraformConvertData,
        )

        return {
            "data": (SecurityMonitoringTerraformConvertData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SecurityMonitoringTerraformConvertData, **kwargs):
        """
        Request body for converting a security monitoring resource JSON to Terraform.

        :param data: The convert request data object.
        :type data: SecurityMonitoringTerraformConvertData
        """
        super().__init__(kwargs)

        self_.data = data
