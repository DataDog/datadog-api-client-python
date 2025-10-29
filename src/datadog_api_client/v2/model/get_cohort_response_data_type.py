# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GetCohortResponseDataType(ModelSimple):
    """


    :param value: If omitted defaults to "cohort_response". Must be one of ["cohort_response"].
    :type value: str
    """

    allowed_values = {
        "cohort_response",
    }
    COHORT_RESPONSE: ClassVar["GetCohortResponseDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GetCohortResponseDataType.COHORT_RESPONSE = GetCohortResponseDataType("cohort_response")
