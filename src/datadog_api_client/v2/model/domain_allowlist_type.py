# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DomainAllowlistType(ModelSimple):
    """
    Email domain allowlist allowlist type.

    :param value: If omitted defaults to "domain_allowlist". Must be one of ["domain_allowlist"].
    :type value: str
    """

    allowed_values = {
        "domain_allowlist",
    }
    DOMAIN_ALLOWLIST: ClassVar["DomainAllowlistType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DomainAllowlistType.DOMAIN_ALLOWLIST = DomainAllowlistType("domain_allowlist")
