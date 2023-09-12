# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CustomDestinationCompressionType(ModelSimple):
    """
    The compression method used for the custom destination.

    :param value: Must be one of ["GZIP", "NONE"].
    :type value: str
    """

    allowed_values = {
        "GZIP",
        "NONE",
    }
    GZIP_COMPRESSION: ClassVar["CustomDestinationCompressionType"]
    NO_COMPRESSION: ClassVar["CustomDestinationCompressionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CustomDestinationCompressionType.GZIP_COMPRESSION = CustomDestinationCompressionType("GZIP")
CustomDestinationCompressionType.NO_COMPRESSION = CustomDestinationCompressionType("NONE")
