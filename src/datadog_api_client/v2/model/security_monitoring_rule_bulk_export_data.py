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
    from datadog_api_client.v2.model.security_monitoring_rule_bulk_export_attributes import (
        SecurityMonitoringRuleBulkExportAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_rule_bulk_export_data_type import (
        SecurityMonitoringRuleBulkExportDataType,
    )


class SecurityMonitoringRuleBulkExportData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_bulk_export_attributes import (
            SecurityMonitoringRuleBulkExportAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_rule_bulk_export_data_type import (
            SecurityMonitoringRuleBulkExportDataType,
        )

        return {
            "attributes": (SecurityMonitoringRuleBulkExportAttributes,),
            "id": (str,),
            "type": (SecurityMonitoringRuleBulkExportDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringRuleBulkExportAttributes,
        type: SecurityMonitoringRuleBulkExportDataType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data for bulk exporting security monitoring rules.

        :param attributes: Attributes for bulk exporting security monitoring rules.
        :type attributes: SecurityMonitoringRuleBulkExportAttributes

        :param id: Request ID.
        :type id: str, optional

        :param type: The type of the resource.
        :type type: SecurityMonitoringRuleBulkExportDataType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
