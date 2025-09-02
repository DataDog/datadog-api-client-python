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
    from datadog_api_client.v2.model.observability_pipeline_socket_source_framing_bytes_method import (
        ObservabilityPipelineSocketSourceFramingBytesMethod,
    )


class ObservabilityPipelineSocketSourceFramingBytes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_socket_source_framing_bytes_method import (
            ObservabilityPipelineSocketSourceFramingBytesMethod,
        )

        return {
            "method": (ObservabilityPipelineSocketSourceFramingBytesMethod,),
        }

    attribute_map = {
        "method": "method",
    }

    def __init__(self_, method: ObservabilityPipelineSocketSourceFramingBytesMethod, **kwargs):
        """
        Byte frames are passed through as-is according to the underlying I/O boundaries (for example, split between messages or stream segments).

        :param method: Byte frames are passed through as-is according to the underlying I/O boundaries (for example, split between messages or stream segments).
        :type method: ObservabilityPipelineSocketSourceFramingBytesMethod
        """
        super().__init__(kwargs)

        self_.method = method
