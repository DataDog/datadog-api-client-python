# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TagPolicyCreateType(ModelSimple):
    """
    The policy type allowed when creating a tag policy. Only `surfacing` is accepted at
        creation time.

    :param value: If omitted defaults to "surfacing". Must be one of ["surfacing"].
    :type value: str
    """

    allowed_values = {
        "surfacing",
    }
    SURFACING: ClassVar["TagPolicyCreateType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TagPolicyCreateType.SURFACING = TagPolicyCreateType("surfacing")
