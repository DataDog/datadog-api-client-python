# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TimeseriesAnomalyInvestigationResponseID(ModelSimple):
    """
    Stable identifier for an anomaly investigation response resource.

    :param value: If omitted defaults to "0". Must be one of ["0"].
    :type value: str
    """

    allowed_values = {
        "0",
    }
    ZERO: ClassVar["TimeseriesAnomalyInvestigationResponseID"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TimeseriesAnomalyInvestigationResponseID.ZERO = TimeseriesAnomalyInvestigationResponseID("0")
