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
    from datadog_api_client.v2.model.security_monitoring_rule_bulk_delete_attributes import (
        SecurityMonitoringRuleBulkDeleteAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_rule_bulk_delete_request_data_type import (
        SecurityMonitoringRuleBulkDeleteRequestDataType,
    )


class SecurityMonitoringRuleBulkDeleteData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_bulk_delete_attributes import (
            SecurityMonitoringRuleBulkDeleteAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_rule_bulk_delete_request_data_type import (
            SecurityMonitoringRuleBulkDeleteRequestDataType,
        )

        return {
            "attributes": (SecurityMonitoringRuleBulkDeleteAttributes,),
            "type": (SecurityMonitoringRuleBulkDeleteRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringRuleBulkDeleteAttributes,
        type: SecurityMonitoringRuleBulkDeleteRequestDataType,
        **kwargs,
    ):
        """
        Data for bulk deleting security monitoring rules.

        :param attributes: Attributes for bulk deleting security monitoring rules.
        :type attributes: SecurityMonitoringRuleBulkDeleteAttributes

        :param type: The resource type for a bulk delete request.
        :type type: SecurityMonitoringRuleBulkDeleteRequestDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
