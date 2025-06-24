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
    from datadog_api_client.v2.model.observability_pipeline_socket_source_framing_octet_counting_method import (
        ObservabilityPipelineSocketSourceFramingOctetCountingMethod,
    )


class ObservabilityPipelineSocketSourceFramingOctetCounting(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_socket_source_framing_octet_counting_method import (
            ObservabilityPipelineSocketSourceFramingOctetCountingMethod,
        )

        return {
            "method": (ObservabilityPipelineSocketSourceFramingOctetCountingMethod,),
        }

    attribute_map = {
        "method": "method",
    }

    def __init__(self_, method: ObservabilityPipelineSocketSourceFramingOctetCountingMethod, **kwargs):
        """
        Byte frames according to the octet counting format as per RFC6587.

        :param method: Byte frames according to the octet counting format as per RFC6587.
        :type method: ObservabilityPipelineSocketSourceFramingOctetCountingMethod
        """
        super().__init__(kwargs)

        self_.method = method
