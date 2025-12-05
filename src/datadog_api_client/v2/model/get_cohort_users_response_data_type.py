# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GetCohortUsersResponseDataType(ModelSimple):
    """


    :param value: If omitted defaults to "cohort_users_response". Must be one of ["cohort_users_response"].
    :type value: str
    """

    allowed_values = {
        "cohort_users_response",
    }
    COHORT_USERS_RESPONSE: ClassVar["GetCohortUsersResponseDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GetCohortUsersResponseDataType.COHORT_USERS_RESPONSE = GetCohortUsersResponseDataType("cohort_users_response")
