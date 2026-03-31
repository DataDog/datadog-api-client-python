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
    from datadog_api_client.v2.model.security_monitoring_signals_bulk_triage_event import (
        SecurityMonitoringSignalsBulkTriageEvent,
    )


class SecurityMonitoringSignalsBulkTriageUpdateResult(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signals_bulk_triage_event import (
            SecurityMonitoringSignalsBulkTriageEvent,
        )

        return {
            "count": (int,),
            "events": ([SecurityMonitoringSignalsBulkTriageEvent],),
        }

    attribute_map = {
        "count": "count",
        "events": "events",
    }

    def __init__(self_, count: int, events: List[SecurityMonitoringSignalsBulkTriageEvent], **kwargs):
        """
        The result payload of a bulk signal triage update.

        :param count: The number of signals updated.
        :type count: int

        :param events: The list of updated signals.
        :type events: [SecurityMonitoringSignalsBulkTriageEvent]
        """
        super().__init__(kwargs)

        self_.count = count
        self_.events = events
