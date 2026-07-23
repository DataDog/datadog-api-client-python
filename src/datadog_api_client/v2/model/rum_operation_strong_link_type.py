# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RUMOperationStrongLinkType(ModelSimple):
    """
    The JSON:API type for RUM operation strong link resources.

    :param value: If omitted defaults to "strong_links". Must be one of ["strong_links"].
    :type value: str
    """

    allowed_values = {
        "strong_links",
    }
    STRONG_LINKS: ClassVar["RUMOperationStrongLinkType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RUMOperationStrongLinkType.STRONG_LINKS = RUMOperationStrongLinkType("strong_links")
