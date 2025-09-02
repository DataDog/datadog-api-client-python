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
    from datadog_api_client.v2.model.observability_pipeline_crowd_strike_next_gen_siem_destination_compression_algorithm import (
        ObservabilityPipelineCrowdStrikeNextGenSiemDestinationCompressionAlgorithm,
    )


class ObservabilityPipelineCrowdStrikeNextGenSiemDestinationCompression(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_crowd_strike_next_gen_siem_destination_compression_algorithm import (
            ObservabilityPipelineCrowdStrikeNextGenSiemDestinationCompressionAlgorithm,
        )

        return {
            "algorithm": (ObservabilityPipelineCrowdStrikeNextGenSiemDestinationCompressionAlgorithm,),
            "level": (int,),
        }

    attribute_map = {
        "algorithm": "algorithm",
        "level": "level",
    }

    def __init__(
        self_,
        algorithm: ObservabilityPipelineCrowdStrikeNextGenSiemDestinationCompressionAlgorithm,
        level: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Compression configuration for log events.

        :param algorithm: Compression algorithm for log events.
        :type algorithm: ObservabilityPipelineCrowdStrikeNextGenSiemDestinationCompressionAlgorithm

        :param level: Compression level.
        :type level: int, optional
        """
        if level is not unset:
            kwargs["level"] = level
        super().__init__(kwargs)

        self_.algorithm = algorithm
