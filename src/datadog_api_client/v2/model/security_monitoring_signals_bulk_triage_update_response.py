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
    from datadog_api_client.v2.model.security_monitoring_signals_bulk_triage_update_result import (
        SecurityMonitoringSignalsBulkTriageUpdateResult,
    )


class SecurityMonitoringSignalsBulkTriageUpdateResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signals_bulk_triage_update_result import (
            SecurityMonitoringSignalsBulkTriageUpdateResult,
        )

        return {
            "result": (SecurityMonitoringSignalsBulkTriageUpdateResult,),
            "status": (str,),
            "type": (str,),
        }

    attribute_map = {
        "result": "result",
        "status": "status",
        "type": "type",
    }

    def __init__(self_, result: SecurityMonitoringSignalsBulkTriageUpdateResult, status: str, type: str, **kwargs):
        """
        Response for a bulk triage update of security signals.

        :param result: The result payload of a bulk signal triage update.
        :type result: SecurityMonitoringSignalsBulkTriageUpdateResult

        :param status: The status of the bulk operation.
        :type status: str

        :param type: The type of the response.
        :type type: str
        """
        super().__init__(kwargs)

        self_.result = result
        self_.status = status
        self_.type = type
