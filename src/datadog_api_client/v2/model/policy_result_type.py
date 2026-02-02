# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class PolicyResultType(ModelSimple):
    """
    The type of the resource. The value should always be `policy_result`.

    :param value: If omitted defaults to "policy_result". Must be one of ["policy_result"].
    :type value: str
    """

    allowed_values = {
        "policy_result",
    }
    POLICY_RESULT: ClassVar["PolicyResultType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


PolicyResultType.POLICY_RESULT = PolicyResultType("policy_result")
