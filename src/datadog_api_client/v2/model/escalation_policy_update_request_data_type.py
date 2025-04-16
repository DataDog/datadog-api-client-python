# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class EscalationPolicyUpdateRequestDataType(ModelSimple):
    """
    Indicates that the resource is of type `policies`.

    :param value: If omitted defaults to "policies". Must be one of ["policies"].
    :type value: str
    """

    allowed_values = {
        "policies",
    }
    POLICIES: ClassVar["EscalationPolicyUpdateRequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EscalationPolicyUpdateRequestDataType.POLICIES = EscalationPolicyUpdateRequestDataType("policies")
