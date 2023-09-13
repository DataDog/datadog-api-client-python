# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class S3FallbackDestinationType(ModelSimple):
    """
    Type of the S3 archive destination.

    :param value: If omitted defaults to "s3". Must be one of ["s3"].
    :type value: str
    """

    allowed_values = {
        "s3",
    }
    S3: ClassVar["S3FallbackDestinationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


S3FallbackDestinationType.S3 = S3FallbackDestinationType("s3")
