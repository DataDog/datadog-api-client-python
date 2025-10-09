# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ReferenceTableCreateSourceType(ModelSimple):
    """
    The source type for creating reference table data. Only these source types can be created through this API.

    :param value: Must be one of ["LOCAL_FILE", "S3", "GCS", "AZURE"].
    :type value: str
    """

    allowed_values = {
        "LOCAL_FILE",
        "S3",
        "GCS",
        "AZURE",
    }
    LOCAL_FILE: ClassVar["ReferenceTableCreateSourceType"]
    S3: ClassVar["ReferenceTableCreateSourceType"]
    GCS: ClassVar["ReferenceTableCreateSourceType"]
    AZURE: ClassVar["ReferenceTableCreateSourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ReferenceTableCreateSourceType.LOCAL_FILE = ReferenceTableCreateSourceType("LOCAL_FILE")
ReferenceTableCreateSourceType.S3 = ReferenceTableCreateSourceType("S3")
ReferenceTableCreateSourceType.GCS = ReferenceTableCreateSourceType("GCS")
ReferenceTableCreateSourceType.AZURE = ReferenceTableCreateSourceType("AZURE")
