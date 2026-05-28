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
    from datadog_api_client.v2.model.summarized_span import SummarizedSpan


class SummarizedTrace(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.summarized_span import SummarizedSpan

        return {
            "root": (SummarizedSpan,),
            "trace_id": (str,),
        }

    attribute_map = {
        "root": "root",
        "trace_id": "traceId",
    }

    def __init__(self_, root: SummarizedSpan, trace_id: str, **kwargs):
        """
        A summarized, hierarchical view of a trace.

        :param root: A node in the pruned trace tree.
        :type root: SummarizedSpan

        :param trace_id: The full 128-bit trace ID, encoded as a 32-character hexadecimal string.
        :type trace_id: str
        """
        super().__init__(kwargs)

        self_.root = root
        self_.trace_id = trace_id
