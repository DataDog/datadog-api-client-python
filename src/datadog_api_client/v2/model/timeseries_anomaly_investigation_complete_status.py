# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TimeseriesAnomalyInvestigationCompleteStatus(ModelSimple):
    """
    Status value indicating successful completion.

    :param value: If omitted defaults to "complete". Must be one of ["complete"].
    :type value: str
    """

    allowed_values = {
        "complete",
    }
    COMPLETE: ClassVar["TimeseriesAnomalyInvestigationCompleteStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TimeseriesAnomalyInvestigationCompleteStatus.COMPLETE = TimeseriesAnomalyInvestigationCompleteStatus("complete")
