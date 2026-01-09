# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineKafkaDestinationCompression(ModelSimple):
    """
    Compression codec for Kafka messages.

    :param value: Must be one of ["none", "gzip", "snappy", "lz4", "zstd"].
    :type value: str
    """

    allowed_values = {
        "none",
        "gzip",
        "snappy",
        "lz4",
        "zstd",
    }
    NONE: ClassVar["ObservabilityPipelineKafkaDestinationCompression"]
    GZIP: ClassVar["ObservabilityPipelineKafkaDestinationCompression"]
    SNAPPY: ClassVar["ObservabilityPipelineKafkaDestinationCompression"]
    LZ4: ClassVar["ObservabilityPipelineKafkaDestinationCompression"]
    ZSTD: ClassVar["ObservabilityPipelineKafkaDestinationCompression"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineKafkaDestinationCompression.NONE = ObservabilityPipelineKafkaDestinationCompression("none")
ObservabilityPipelineKafkaDestinationCompression.GZIP = ObservabilityPipelineKafkaDestinationCompression("gzip")
ObservabilityPipelineKafkaDestinationCompression.SNAPPY = ObservabilityPipelineKafkaDestinationCompression("snappy")
ObservabilityPipelineKafkaDestinationCompression.LZ4 = ObservabilityPipelineKafkaDestinationCompression("lz4")
ObservabilityPipelineKafkaDestinationCompression.ZSTD = ObservabilityPipelineKafkaDestinationCompression("zstd")
