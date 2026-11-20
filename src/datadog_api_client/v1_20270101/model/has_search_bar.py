# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class HasSearchBar(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["auto", "always", "never"].
    :type value: str
    """

    allowed_values = {
        "auto",
        "always",
        "never",
    }
    AUTO: ClassVar["HasSearchBar"]
    ALWAYS: ClassVar["HasSearchBar"]
    NEVER: ClassVar["HasSearchBar"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


HasSearchBar.AUTO = HasSearchBar("auto")
HasSearchBar.ALWAYS = HasSearchBar("always")
HasSearchBar.NEVER = HasSearchBar("never")
