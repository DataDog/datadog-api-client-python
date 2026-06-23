# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_clickhouse_destination_compression_algorithm import (
        ObservabilityPipelineClickhouseDestinationCompressionAlgorithm,
    )


class ObservabilityPipelineClickhouseDestinationCompressionObject(ModelNormal):
    validations = {
        "level": {
            "inclusive_maximum": 9,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_clickhouse_destination_compression_algorithm import (
            ObservabilityPipelineClickhouseDestinationCompressionAlgorithm,
        )

        return {
            "algorithm": (ObservabilityPipelineClickhouseDestinationCompressionAlgorithm,),
            "level": (int,),
        }

    attribute_map = {
        "algorithm": "algorithm",
        "level": "level",
    }

    def __init__(
        self_,
        algorithm: ObservabilityPipelineClickhouseDestinationCompressionAlgorithm,
        level: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Structured compression configuration for the ClickHouse destination.
        Use ``algorithm`` to specify the compression type and ``level`` (optional, gzip only) to control compression strength.

        :param algorithm: The compression algorithm applied to outbound HTTP requests.
        :type algorithm: ObservabilityPipelineClickhouseDestinationCompressionAlgorithm

        :param level: Compression level (1–9). Only applicable when ``algorithm`` is ``gzip``.
        :type level: int, optional
        """
        if level is not unset:
            kwargs["level"] = level
        super().__init__(kwargs)

        self_.algorithm = algorithm
