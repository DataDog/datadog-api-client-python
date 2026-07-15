# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AccountFiltersPatchRequestType(ModelSimple):
    """
    Type of account filters patch request.

    :param value: If omitted defaults to "account_filters_patch_request". Must be one of ["account_filters_patch_request"].
    :type value: str
    """

    allowed_values = {
        "account_filters_patch_request",
    }
    ACCOUNT_FILTERS_PATCH_REQUEST: ClassVar["AccountFiltersPatchRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AccountFiltersPatchRequestType.ACCOUNT_FILTERS_PATCH_REQUEST = AccountFiltersPatchRequestType(
    "account_filters_patch_request"
)
