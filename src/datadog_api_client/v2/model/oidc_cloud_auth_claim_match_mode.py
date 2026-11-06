# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OIDCCloudAuthClaimMatchMode(ModelSimple):
    """
    Case-sensitive matching mode. Exact compares strings. Glob matches the entire value: * matches any number of characters, including /, and ? matches one character. Other characters are literal; escaping is not supported.

    :param value: If omitted defaults to "exact". Must be one of ["exact", "glob"].
    :type value: str
    """

    allowed_values = {
        "exact",
        "glob",
    }
    EXACT: ClassVar["OIDCCloudAuthClaimMatchMode"]
    GLOB: ClassVar["OIDCCloudAuthClaimMatchMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OIDCCloudAuthClaimMatchMode.EXACT = OIDCCloudAuthClaimMatchMode("exact")
OIDCCloudAuthClaimMatchMode.GLOB = OIDCCloudAuthClaimMatchMode("glob")
