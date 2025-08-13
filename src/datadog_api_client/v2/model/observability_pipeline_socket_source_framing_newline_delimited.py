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
    from datadog_api_client.v2.model.observability_pipeline_socket_source_framing_newline_delimited_method import (
        ObservabilityPipelineSocketSourceFramingNewlineDelimitedMethod,
    )


class ObservabilityPipelineSocketSourceFramingNewlineDelimited(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_socket_source_framing_newline_delimited_method import (
            ObservabilityPipelineSocketSourceFramingNewlineDelimitedMethod,
        )

        return {
            "method": (ObservabilityPipelineSocketSourceFramingNewlineDelimitedMethod,),
        }

    attribute_map = {
        "method": "method",
    }

    def __init__(self_, method: ObservabilityPipelineSocketSourceFramingNewlineDelimitedMethod, **kwargs):
        """
        Byte frames which are delimited by a newline character.

        :param method: Byte frames which are delimited by a newline character.
        :type method: ObservabilityPipelineSocketSourceFramingNewlineDelimitedMethod
        """
        super().__init__(kwargs)

        self_.method = method
