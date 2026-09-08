# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TimeseriesAnomalyInvestigationQueryExecutionStatus(ModelSimple):
    """
    Current execution status for a named query.

    :param value: Must be one of ["running", "done"].
    :type value: str
    """

    allowed_values = {
        "running",
        "done",
    }
    RUNNING: ClassVar["TimeseriesAnomalyInvestigationQueryExecutionStatus"]
    DONE: ClassVar["TimeseriesAnomalyInvestigationQueryExecutionStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TimeseriesAnomalyInvestigationQueryExecutionStatus.RUNNING = TimeseriesAnomalyInvestigationQueryExecutionStatus(
    "running"
)
TimeseriesAnomalyInvestigationQueryExecutionStatus.DONE = TimeseriesAnomalyInvestigationQueryExecutionStatus("done")
