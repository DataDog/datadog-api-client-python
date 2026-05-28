# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.summarized_trace import SummarizedTrace


class PrunedTraceAttributes(ModelNormal):
    validations = {
        "size_bytes": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.summarized_trace import SummarizedTrace

        return {
            "is_truncated": (bool,),
            "size_bytes": (int,),
            "summarized_trace": (SummarizedTrace,),
        }

    attribute_map = {
        "is_truncated": "is_truncated",
        "size_bytes": "size_bytes",
        "summarized_trace": "summarized_trace",
    }

    def __init__(self_, is_truncated: bool, size_bytes: int, summarized_trace: SummarizedTrace, **kwargs):
        """
        The attributes of a pruned trace returned by the Get pruned trace by ID endpoint.

        :param is_truncated: Indicates whether the underlying trace was truncated because its size
            exceeded the maximum that can be retrieved from storage.
        :type is_truncated: bool

        :param size_bytes: The size, in bytes, of the original (non-pruned) trace before summarization.
        :type size_bytes: int

        :param summarized_trace: A summarized, hierarchical view of a trace.
        :type summarized_trace: SummarizedTrace
        """
        super().__init__(kwargs)

        self_.is_truncated = is_truncated
        self_.size_bytes = size_bytes
        self_.summarized_trace = summarized_trace
