# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_socket_destination_encoding import (
        ObservabilityPipelineSocketDestinationEncoding,
    )
    from datadog_api_client.v2.model.observability_pipeline_socket_destination_framing import (
        ObservabilityPipelineSocketDestinationFraming,
    )
    from datadog_api_client.v2.model.observability_pipeline_socket_destination_mode import (
        ObservabilityPipelineSocketDestinationMode,
    )
    from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
    from datadog_api_client.v2.model.observability_pipeline_socket_destination_type import (
        ObservabilityPipelineSocketDestinationType,
    )
    from datadog_api_client.v2.model.observability_pipeline_socket_destination_framing_newline_delimited import (
        ObservabilityPipelineSocketDestinationFramingNewlineDelimited,
    )
    from datadog_api_client.v2.model.observability_pipeline_socket_destination_framing_bytes import (
        ObservabilityPipelineSocketDestinationFramingBytes,
    )
    from datadog_api_client.v2.model.observability_pipeline_socket_destination_framing_character_delimited import (
        ObservabilityPipelineSocketDestinationFramingCharacterDelimited,
    )


class ObservabilityPipelineSocketDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_socket_destination_encoding import (
            ObservabilityPipelineSocketDestinationEncoding,
        )
        from datadog_api_client.v2.model.observability_pipeline_socket_destination_framing import (
            ObservabilityPipelineSocketDestinationFraming,
        )
        from datadog_api_client.v2.model.observability_pipeline_socket_destination_mode import (
            ObservabilityPipelineSocketDestinationMode,
        )
        from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
        from datadog_api_client.v2.model.observability_pipeline_socket_destination_type import (
            ObservabilityPipelineSocketDestinationType,
        )

        return {
            "encoding": (ObservabilityPipelineSocketDestinationEncoding,),
            "framing": (ObservabilityPipelineSocketDestinationFraming,),
            "id": (str,),
            "inputs": ([str],),
            "mode": (ObservabilityPipelineSocketDestinationMode,),
            "tls": (ObservabilityPipelineTls,),
            "type": (ObservabilityPipelineSocketDestinationType,),
        }

    attribute_map = {
        "encoding": "encoding",
        "framing": "framing",
        "id": "id",
        "inputs": "inputs",
        "mode": "mode",
        "tls": "tls",
        "type": "type",
    }

    def __init__(
        self_,
        encoding: ObservabilityPipelineSocketDestinationEncoding,
        framing: Union[
            ObservabilityPipelineSocketDestinationFraming,
            ObservabilityPipelineSocketDestinationFramingNewlineDelimited,
            ObservabilityPipelineSocketDestinationFramingBytes,
            ObservabilityPipelineSocketDestinationFramingCharacterDelimited,
        ],
        id: str,
        inputs: List[str],
        mode: ObservabilityPipelineSocketDestinationMode,
        type: ObservabilityPipelineSocketDestinationType,
        tls: Union[ObservabilityPipelineTls, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``socket`` destination sends logs over TCP or UDP to a remote server.

        :param encoding: Encoding format for log events.
        :type encoding: ObservabilityPipelineSocketDestinationEncoding

        :param framing: Framing method configuration.
        :type framing: ObservabilityPipelineSocketDestinationFraming

        :param id: The unique identifier for this component.
        :type id: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param mode: Protocol used to send logs.
        :type mode: ObservabilityPipelineSocketDestinationMode

        :param tls: Configuration for enabling TLS encryption between the pipeline component and external services.
        :type tls: ObservabilityPipelineTls, optional

        :param type: The destination type. The value should always be ``socket``.
        :type type: ObservabilityPipelineSocketDestinationType
        """
        if tls is not unset:
            kwargs["tls"] = tls
        super().__init__(kwargs)

        self_.encoding = encoding
        self_.framing = framing
        self_.id = id
        self_.inputs = inputs
        self_.mode = mode
        self_.type = type
