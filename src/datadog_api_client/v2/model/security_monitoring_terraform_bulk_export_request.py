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
    from datadog_api_client.v2.model.security_monitoring_terraform_bulk_export_data import (
        SecurityMonitoringTerraformBulkExportData,
    )


class SecurityMonitoringTerraformBulkExportRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_terraform_bulk_export_data import (
            SecurityMonitoringTerraformBulkExportData,
        )

        return {
            "data": (SecurityMonitoringTerraformBulkExportData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SecurityMonitoringTerraformBulkExportData, **kwargs):
        """
        Request body for bulk exporting security monitoring resources to Terraform.

        :param data: The bulk export request data object.
        :type data: SecurityMonitoringTerraformBulkExportData
        """
        super().__init__(kwargs)

        self_.data = data
