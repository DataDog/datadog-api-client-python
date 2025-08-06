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
    from datadog_api_client.v2.model.observability_pipeline_crowd_strike_next_gen_siem_destination_compression import (
        ObservabilityPipelineCrowdStrikeNextGenSiemDestinationCompression,
    )
    from datadog_api_client.v2.model.observability_pipeline_crowd_strike_next_gen_siem_destination_encoding import (
        ObservabilityPipelineCrowdStrikeNextGenSiemDestinationEncoding,
    )
    from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
    from datadog_api_client.v2.model.observability_pipeline_crowd_strike_next_gen_siem_destination_type import (
        ObservabilityPipelineCrowdStrikeNextGenSiemDestinationType,
    )


class ObservabilityPipelineCrowdStrikeNextGenSiemDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_crowd_strike_next_gen_siem_destination_compression import (
            ObservabilityPipelineCrowdStrikeNextGenSiemDestinationCompression,
        )
        from datadog_api_client.v2.model.observability_pipeline_crowd_strike_next_gen_siem_destination_encoding import (
            ObservabilityPipelineCrowdStrikeNextGenSiemDestinationEncoding,
        )
        from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
        from datadog_api_client.v2.model.observability_pipeline_crowd_strike_next_gen_siem_destination_type import (
            ObservabilityPipelineCrowdStrikeNextGenSiemDestinationType,
        )

        return {
            "compression": (ObservabilityPipelineCrowdStrikeNextGenSiemDestinationCompression,),
            "encoding": (ObservabilityPipelineCrowdStrikeNextGenSiemDestinationEncoding,),
            "id": (str,),
            "inputs": ([str],),
            "tls": (ObservabilityPipelineTls,),
            "type": (ObservabilityPipelineCrowdStrikeNextGenSiemDestinationType,),
        }

    attribute_map = {
        "compression": "compression",
        "encoding": "encoding",
        "id": "id",
        "inputs": "inputs",
        "tls": "tls",
        "type": "type",
    }

    def __init__(
        self_,
        encoding: ObservabilityPipelineCrowdStrikeNextGenSiemDestinationEncoding,
        id: str,
        inputs: List[str],
        type: ObservabilityPipelineCrowdStrikeNextGenSiemDestinationType,
        compression: Union[ObservabilityPipelineCrowdStrikeNextGenSiemDestinationCompression, UnsetType] = unset,
        tls: Union[ObservabilityPipelineTls, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``crowdstrike_next_gen_siem`` destination forwards logs to CrowdStrike Next Gen SIEM.

        :param compression: Compression configuration for log events.
        :type compression: ObservabilityPipelineCrowdStrikeNextGenSiemDestinationCompression, optional

        :param encoding: Encoding format for log events.
        :type encoding: ObservabilityPipelineCrowdStrikeNextGenSiemDestinationEncoding

        :param id: The unique identifier for this component.
        :type id: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param tls: Configuration for enabling TLS encryption between the pipeline component and external services.
        :type tls: ObservabilityPipelineTls, optional

        :param type: The destination type. The value should always be ``crowdstrike_next_gen_siem``.
        :type type: ObservabilityPipelineCrowdStrikeNextGenSiemDestinationType
        """
        if compression is not unset:
            kwargs["compression"] = compression
        if tls is not unset:
            kwargs["tls"] = tls
        super().__init__(kwargs)

        self_.encoding = encoding
        self_.id = id
        self_.inputs = inputs
        self_.type = type
