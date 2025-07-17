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
    from datadog_api_client.v2.model.observability_pipeline_socket_source_framing import (
        ObservabilityPipelineSocketSourceFraming,
    )
    from datadog_api_client.v2.model.observability_pipeline_socket_source_mode import (
        ObservabilityPipelineSocketSourceMode,
    )
    from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
    from datadog_api_client.v2.model.observability_pipeline_socket_source_type import (
        ObservabilityPipelineSocketSourceType,
    )
    from datadog_api_client.v2.model.observability_pipeline_socket_source_framing_newline_delimited import (
        ObservabilityPipelineSocketSourceFramingNewlineDelimited,
    )
    from datadog_api_client.v2.model.observability_pipeline_socket_source_framing_bytes import (
        ObservabilityPipelineSocketSourceFramingBytes,
    )
    from datadog_api_client.v2.model.observability_pipeline_socket_source_framing_character_delimited import (
        ObservabilityPipelineSocketSourceFramingCharacterDelimited,
    )
    from datadog_api_client.v2.model.observability_pipeline_socket_source_framing_octet_counting import (
        ObservabilityPipelineSocketSourceFramingOctetCounting,
    )
    from datadog_api_client.v2.model.observability_pipeline_socket_source_framing_chunked_gelf import (
        ObservabilityPipelineSocketSourceFramingChunkedGelf,
    )


class ObservabilityPipelineSocketSource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_socket_source_framing import (
            ObservabilityPipelineSocketSourceFraming,
        )
        from datadog_api_client.v2.model.observability_pipeline_socket_source_mode import (
            ObservabilityPipelineSocketSourceMode,
        )
        from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
        from datadog_api_client.v2.model.observability_pipeline_socket_source_type import (
            ObservabilityPipelineSocketSourceType,
        )

        return {
            "framing": (ObservabilityPipelineSocketSourceFraming,),
            "id": (str,),
            "mode": (ObservabilityPipelineSocketSourceMode,),
            "tls": (ObservabilityPipelineTls,),
            "type": (ObservabilityPipelineSocketSourceType,),
        }

    attribute_map = {
        "framing": "framing",
        "id": "id",
        "mode": "mode",
        "tls": "tls",
        "type": "type",
    }

    def __init__(
        self_,
        framing: Union[
            ObservabilityPipelineSocketSourceFraming,
            ObservabilityPipelineSocketSourceFramingNewlineDelimited,
            ObservabilityPipelineSocketSourceFramingBytes,
            ObservabilityPipelineSocketSourceFramingCharacterDelimited,
            ObservabilityPipelineSocketSourceFramingOctetCounting,
            ObservabilityPipelineSocketSourceFramingChunkedGelf,
        ],
        id: str,
        mode: ObservabilityPipelineSocketSourceMode,
        type: ObservabilityPipelineSocketSourceType,
        tls: Union[ObservabilityPipelineTls, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``socket`` source ingests logs over TCP or UDP.

        :param framing: Framing method configuration for the socket source.
        :type framing: ObservabilityPipelineSocketSourceFraming

        :param id: The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
        :type id: str

        :param mode: Protocol used to receive logs.
        :type mode: ObservabilityPipelineSocketSourceMode

        :param tls: Configuration for enabling TLS encryption between the pipeline component and external services.
        :type tls: ObservabilityPipelineTls, optional

        :param type: The source type. The value should always be ``socket``.
        :type type: ObservabilityPipelineSocketSourceType
        """
        if tls is not unset:
            kwargs["tls"] = tls
        super().__init__(kwargs)

        self_.framing = framing
        self_.id = id
        self_.mode = mode
        self_.type = type
