# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SLOReportInterval(ModelSimple):
    """
    The frequency at which report data is to be generated.

    :param value: Must be one of ["weekly", "monthly"].
    :type value: str
    """

    allowed_values = {
        "weekly",
        "monthly",
    }
    WEEKLY: ClassVar["SLOReportInterval"]
    MONTHLY: ClassVar["SLOReportInterval"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SLOReportInterval.WEEKLY = SLOReportInterval("weekly")
SLOReportInterval.MONTHLY = SLOReportInterval("monthly")
