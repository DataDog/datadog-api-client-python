# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OnPremManagementServiceRegisterTokenType(ModelSimple):
    """
    The type of the resource. The value should always be registerTokenRequest.

    :param value: If omitted defaults to "registerTokenRequest". Must be one of ["registerTokenRequest"].
    :type value: str
    """

    allowed_values = {
        "registerTokenRequest",
    }
    REGISTERTOKENREQUEST: ClassVar["OnPremManagementServiceRegisterTokenType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OnPremManagementServiceRegisterTokenType.REGISTERTOKENREQUEST = OnPremManagementServiceRegisterTokenType(
    "registerTokenRequest"
)
