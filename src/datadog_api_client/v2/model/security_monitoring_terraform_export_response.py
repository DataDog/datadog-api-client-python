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
    from datadog_api_client.v2.model.security_monitoring_terraform_export_data import (
        SecurityMonitoringTerraformExportData,
    )


class SecurityMonitoringTerraformExportResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_terraform_export_data import (
            SecurityMonitoringTerraformExportData,
        )

        return {
            "data": (SecurityMonitoringTerraformExportData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[SecurityMonitoringTerraformExportData, UnsetType] = unset, **kwargs):
        """
        Response containing the Terraform configuration for a security monitoring resource.

        :param data: The Terraform export data object.
        :type data: SecurityMonitoringTerraformExportData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
