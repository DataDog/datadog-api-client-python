# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AWSNamespacesResponseDataType(ModelSimple):
    """
    The `AWSNamespacesResponseData` `type`.

    :param value: If omitted defaults to "namespaces". Must be one of ["namespaces"].
    :type value: str
    """

    allowed_values = {
        "namespaces",
    }
    NAMESPACES: ClassVar["AWSNamespacesResponseDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AWSNamespacesResponseDataType.NAMESPACES = AWSNamespacesResponseDataType("namespaces")
