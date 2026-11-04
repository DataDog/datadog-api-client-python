# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CommitmentsListResponseType(ModelSimple):
    """
    Type of the commitments list response resource.

    :param value: If omitted defaults to "commitments_list_response". Must be one of ["commitments_list_response"].
    :type value: str
    """

    allowed_values = {
        "commitments_list_response",
    }
    COMMITMENTS_LIST_RESPONSE: ClassVar["CommitmentsListResponseType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CommitmentsListResponseType.COMMITMENTS_LIST_RESPONSE = CommitmentsListResponseType("commitments_list_response")
