# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineReduceProcessorMergeStrategyStrategy(ModelSimple):
    """
    The merge strategy to apply.

    :param value: Must be one of ["discard", "retain", "sum", "max", "min", "array", "concat", "concat_newline", "concat_raw", "shortest_array", "longest_array", "flat_unique"].
    :type value: str
    """

    allowed_values = {
        "discard",
        "retain",
        "sum",
        "max",
        "min",
        "array",
        "concat",
        "concat_newline",
        "concat_raw",
        "shortest_array",
        "longest_array",
        "flat_unique",
    }
    DISCARD: ClassVar["ObservabilityPipelineReduceProcessorMergeStrategyStrategy"]
    RETAIN: ClassVar["ObservabilityPipelineReduceProcessorMergeStrategyStrategy"]
    SUM: ClassVar["ObservabilityPipelineReduceProcessorMergeStrategyStrategy"]
    MAX: ClassVar["ObservabilityPipelineReduceProcessorMergeStrategyStrategy"]
    MIN: ClassVar["ObservabilityPipelineReduceProcessorMergeStrategyStrategy"]
    ARRAY: ClassVar["ObservabilityPipelineReduceProcessorMergeStrategyStrategy"]
    CONCAT: ClassVar["ObservabilityPipelineReduceProcessorMergeStrategyStrategy"]
    CONCAT_NEWLINE: ClassVar["ObservabilityPipelineReduceProcessorMergeStrategyStrategy"]
    CONCAT_RAW: ClassVar["ObservabilityPipelineReduceProcessorMergeStrategyStrategy"]
    SHORTEST_ARRAY: ClassVar["ObservabilityPipelineReduceProcessorMergeStrategyStrategy"]
    LONGEST_ARRAY: ClassVar["ObservabilityPipelineReduceProcessorMergeStrategyStrategy"]
    FLAT_UNIQUE: ClassVar["ObservabilityPipelineReduceProcessorMergeStrategyStrategy"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineReduceProcessorMergeStrategyStrategy.DISCARD = (
    ObservabilityPipelineReduceProcessorMergeStrategyStrategy("discard")
)
ObservabilityPipelineReduceProcessorMergeStrategyStrategy.RETAIN = (
    ObservabilityPipelineReduceProcessorMergeStrategyStrategy("retain")
)
ObservabilityPipelineReduceProcessorMergeStrategyStrategy.SUM = (
    ObservabilityPipelineReduceProcessorMergeStrategyStrategy("sum")
)
ObservabilityPipelineReduceProcessorMergeStrategyStrategy.MAX = (
    ObservabilityPipelineReduceProcessorMergeStrategyStrategy("max")
)
ObservabilityPipelineReduceProcessorMergeStrategyStrategy.MIN = (
    ObservabilityPipelineReduceProcessorMergeStrategyStrategy("min")
)
ObservabilityPipelineReduceProcessorMergeStrategyStrategy.ARRAY = (
    ObservabilityPipelineReduceProcessorMergeStrategyStrategy("array")
)
ObservabilityPipelineReduceProcessorMergeStrategyStrategy.CONCAT = (
    ObservabilityPipelineReduceProcessorMergeStrategyStrategy("concat")
)
ObservabilityPipelineReduceProcessorMergeStrategyStrategy.CONCAT_NEWLINE = (
    ObservabilityPipelineReduceProcessorMergeStrategyStrategy("concat_newline")
)
ObservabilityPipelineReduceProcessorMergeStrategyStrategy.CONCAT_RAW = (
    ObservabilityPipelineReduceProcessorMergeStrategyStrategy("concat_raw")
)
ObservabilityPipelineReduceProcessorMergeStrategyStrategy.SHORTEST_ARRAY = (
    ObservabilityPipelineReduceProcessorMergeStrategyStrategy("shortest_array")
)
ObservabilityPipelineReduceProcessorMergeStrategyStrategy.LONGEST_ARRAY = (
    ObservabilityPipelineReduceProcessorMergeStrategyStrategy("longest_array")
)
ObservabilityPipelineReduceProcessorMergeStrategyStrategy.FLAT_UNIQUE = (
    ObservabilityPipelineReduceProcessorMergeStrategyStrategy("flat_unique")
)
