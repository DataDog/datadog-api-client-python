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
    from datadog_api_client.v2.model.security_monitoring_terraform_bulk_export_attributes import (
        SecurityMonitoringTerraformBulkExportAttributes,
    )


class SecurityMonitoringTerraformBulkExportData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_terraform_bulk_export_attributes import (
            SecurityMonitoringTerraformBulkExportAttributes,
        )

        return {
            "attributes": (SecurityMonitoringTerraformBulkExportAttributes,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: SecurityMonitoringTerraformBulkExportAttributes, type: str, **kwargs):
        """
        The bulk export request data object.

        :param attributes: Attributes for the bulk export request.
        :type attributes: SecurityMonitoringTerraformBulkExportAttributes

        :param type: The JSON:API type. Always ``bulk_export_resources``.
        :type type: str
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
