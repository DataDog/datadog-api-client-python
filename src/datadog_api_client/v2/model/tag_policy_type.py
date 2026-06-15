# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TagPolicyType(ModelSimple):
    """
    How the policy is enforced. `blocking` rejects telemetry that violates the policy.
        `surfacing` only highlights non-compliant telemetry without blocking it.

    :param value: Must be one of ["blocking", "surfacing"].
    :type value: str
    """

    allowed_values = {
        "blocking",
        "surfacing",
    }
    BLOCKING: ClassVar["TagPolicyType"]
    SURFACING: ClassVar["TagPolicyType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TagPolicyType.BLOCKING = TagPolicyType("blocking")
TagPolicyType.SURFACING = TagPolicyType("surfacing")
