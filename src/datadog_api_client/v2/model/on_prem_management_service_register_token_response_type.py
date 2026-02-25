# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OnPremManagementServiceRegisterTokenResponseType(ModelSimple):
    """
    The type of the resource. The value should always be tokenDefinitions.

    :param value: If omitted defaults to "tokenDefinitions". Must be one of ["tokenDefinitions"].
    :type value: str
    """

    allowed_values = {
        "tokenDefinitions",
    }
    TOKENDEFINITIONS: ClassVar["OnPremManagementServiceRegisterTokenResponseType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OnPremManagementServiceRegisterTokenResponseType.TOKENDEFINITIONS = OnPremManagementServiceRegisterTokenResponseType(
    "tokenDefinitions"
)
