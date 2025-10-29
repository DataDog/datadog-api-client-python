# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GetCohortUsersRequestDataType(ModelSimple):
    """


    :param value: If omitted defaults to "cohort_users_request". Must be one of ["cohort_users_request"].
    :type value: str
    """

    allowed_values = {
        "cohort_users_request",
    }
    COHORT_USERS_REQUEST: ClassVar["GetCohortUsersRequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GetCohortUsersRequestDataType.COHORT_USERS_REQUEST = GetCohortUsersRequestDataType("cohort_users_request")
