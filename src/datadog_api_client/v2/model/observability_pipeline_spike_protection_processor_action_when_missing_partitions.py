# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineSpikeProtectionProcessorActionWhenMissingPartitions(ModelSimple):
    """
    How to handle logs that are missing one of the `partition_fields`. Options:
        - `ignore`: Forward the event without applying spike protection.
        - `default_bucket`: Assign the event to a default partition.

    :param value: If omitted defaults to "ignore". Must be one of ["ignore", "default_bucket"].
    :type value: str
    """

    allowed_values = {
        "ignore",
        "default_bucket",
    }
    IGNORE: ClassVar["ObservabilityPipelineSpikeProtectionProcessorActionWhenMissingPartitions"]
    DEFAULT_BUCKET: ClassVar["ObservabilityPipelineSpikeProtectionProcessorActionWhenMissingPartitions"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineSpikeProtectionProcessorActionWhenMissingPartitions.IGNORE = (
    ObservabilityPipelineSpikeProtectionProcessorActionWhenMissingPartitions("ignore")
)
ObservabilityPipelineSpikeProtectionProcessorActionWhenMissingPartitions.DEFAULT_BUCKET = (
    ObservabilityPipelineSpikeProtectionProcessorActionWhenMissingPartitions("default_bucket")
)
