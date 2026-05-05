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
    from datadog_api_client.v2.model.security_monitoring_rule_bulk_delete_data import (
        SecurityMonitoringRuleBulkDeleteData,
    )


class SecurityMonitoringRuleBulkDeletePayload(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_bulk_delete_data import (
            SecurityMonitoringRuleBulkDeleteData,
        )

        return {
            "data": (SecurityMonitoringRuleBulkDeleteData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SecurityMonitoringRuleBulkDeleteData, **kwargs):
        """
        Payload for bulk deleting security monitoring rules.

        :param data: Data for bulk deleting security monitoring rules.
        :type data: SecurityMonitoringRuleBulkDeleteData
        """
        super().__init__(kwargs)

        self_.data = data
