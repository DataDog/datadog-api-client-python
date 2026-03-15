# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineAmazonS3GenericEncodingParquetType(ModelSimple):
    """
    The encoding type. Always `parquet`.

    :param value: If omitted defaults to "parquet". Must be one of ["parquet"].
    :type value: str
    """

    allowed_values = {
        "parquet",
    }
    PARQUET: ClassVar["ObservabilityPipelineAmazonS3GenericEncodingParquetType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineAmazonS3GenericEncodingParquetType.PARQUET = (
    ObservabilityPipelineAmazonS3GenericEncodingParquetType("parquet")
)
