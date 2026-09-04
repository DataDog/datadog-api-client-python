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
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_query_execution_status import (
        TimeseriesAnomalyInvestigationQueryExecutionStatus,
    )


class TimeseriesAnomalyInvestigationQueryStatus(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_query_execution_status import (
            TimeseriesAnomalyInvestigationQueryExecutionStatus,
        )

        return {
            "name": (str,),
            "status": (TimeseriesAnomalyInvestigationQueryExecutionStatus,),
        }

    attribute_map = {
        "name": "name",
        "status": "status",
    }

    def __init__(self_, name: str, status: TimeseriesAnomalyInvestigationQueryExecutionStatus, **kwargs):
        """
        Execution status for one named query.

        :param name: Query name from the request.
        :type name: str

        :param status: Current execution status for a named query.
        :type status: TimeseriesAnomalyInvestigationQueryExecutionStatus
        """
        super().__init__(kwargs)

        self_.name = name
        self_.status = status
