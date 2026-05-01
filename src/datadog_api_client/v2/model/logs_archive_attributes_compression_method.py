# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LogsArchiveAttributesCompressionMethod(ModelSimple):
    """
    The type of compression for the archive.

    :param value: If omitted defaults to "GZIP". Must be one of ["GZIP", "ZSTD"].
    :type value: str
    """

    allowed_values = {
        "GZIP",
        "ZSTD",
    }
    GZIP: ClassVar["LogsArchiveAttributesCompressionMethod"]
    ZSTD: ClassVar["LogsArchiveAttributesCompressionMethod"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LogsArchiveAttributesCompressionMethod.GZIP = LogsArchiveAttributesCompressionMethod("GZIP")
LogsArchiveAttributesCompressionMethod.ZSTD = LogsArchiveAttributesCompressionMethod("ZSTD")
