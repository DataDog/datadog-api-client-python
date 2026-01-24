# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SloStatusType(ModelSimple):
    """
    The type of the SLO status resource.

    :param value: If omitted defaults to "slo_status". Must be one of ["slo_status"].
    :type value: str
    """

    allowed_values = {
        "slo_status",
    }
    SLO_STATUS: ClassVar["SloStatusType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SloStatusType.SLO_STATUS = SloStatusType("slo_status")
