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
    from datadog_api_client.v2.model.security_monitoring_signals_bulk_assignee_update_data import (
        SecurityMonitoringSignalsBulkAssigneeUpdateData,
    )


class SecurityMonitoringSignalsBulkAssigneeUpdateRequest(ModelNormal):
    validations = {
        "data": {
            "max_items": 199,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signals_bulk_assignee_update_data import (
            SecurityMonitoringSignalsBulkAssigneeUpdateData,
        )

        return {
            "data": ([SecurityMonitoringSignalsBulkAssigneeUpdateData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[SecurityMonitoringSignalsBulkAssigneeUpdateData], **kwargs):
        """
        Request body for updating the assignee of multiple security signals.

        :param data: An array of signal assignee updates.
        :type data: [SecurityMonitoringSignalsBulkAssigneeUpdateData]
        """
        super().__init__(kwargs)

        self_.data = data
