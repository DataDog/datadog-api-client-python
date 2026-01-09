# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GetCohortRequestDataType(ModelSimple):
    """


    :param value: If omitted defaults to "cohort_request". Must be one of ["cohort_request"].
    :type value: str
    """

    allowed_values = {
        "cohort_request",
    }
    COHORT_REQUEST: ClassVar["GetCohortRequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GetCohortRequestDataType.COHORT_REQUEST = GetCohortRequestDataType("cohort_request")
