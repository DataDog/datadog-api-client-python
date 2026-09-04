# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TimeseriesAnomalyInvestigationTagAnalysisStatus(ModelSimple):
    """
    Outcome of optional influential-tag enrichment.

    :param value: Must be one of ["complete", "unsupported", "failed"].
    :type value: str
    """

    allowed_values = {
        "complete",
        "unsupported",
        "failed",
    }
    COMPLETE: ClassVar["TimeseriesAnomalyInvestigationTagAnalysisStatus"]
    UNSUPPORTED: ClassVar["TimeseriesAnomalyInvestigationTagAnalysisStatus"]
    FAILED: ClassVar["TimeseriesAnomalyInvestigationTagAnalysisStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TimeseriesAnomalyInvestigationTagAnalysisStatus.COMPLETE = TimeseriesAnomalyInvestigationTagAnalysisStatus("complete")
TimeseriesAnomalyInvestigationTagAnalysisStatus.UNSUPPORTED = TimeseriesAnomalyInvestigationTagAnalysisStatus(
    "unsupported"
)
TimeseriesAnomalyInvestigationTagAnalysisStatus.FAILED = TimeseriesAnomalyInvestigationTagAnalysisStatus("failed")
