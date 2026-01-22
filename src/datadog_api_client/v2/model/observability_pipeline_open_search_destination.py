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
    from datadog_api_client.v2.model.observability_pipeline_open_search_destination_data_stream import (
        ObservabilityPipelineOpenSearchDestinationDataStream,
    )
    from datadog_api_client.v2.model.observability_pipeline_open_search_destination_type import (
        ObservabilityPipelineOpenSearchDestinationType,
    )


class ObservabilityPipelineOpenSearchDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_open_search_destination_data_stream import (
            ObservabilityPipelineOpenSearchDestinationDataStream,
        )
        from datadog_api_client.v2.model.observability_pipeline_open_search_destination_type import (
            ObservabilityPipelineOpenSearchDestinationType,
        )

        return {
            "bulk_index": (str,),
            "data_stream": (ObservabilityPipelineOpenSearchDestinationDataStream,),
            "id": (str,),
            "inputs": ([str],),
            "type": (ObservabilityPipelineOpenSearchDestinationType,),
        }

    attribute_map = {
        "bulk_index": "bulk_index",
        "data_stream": "data_stream",
        "id": "id",
        "inputs": "inputs",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        inputs: List[str],
        type: ObservabilityPipelineOpenSearchDestinationType,
        bulk_index: Union[str, UnsetType] = unset,
        data_stream: Union[ObservabilityPipelineOpenSearchDestinationDataStream, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``opensearch`` destination writes logs to an OpenSearch cluster.

        **Supported pipeline types:** logs

        :param bulk_index: The index to write logs to.
        :type bulk_index: str, optional

        :param data_stream: Configuration options for writing to OpenSearch Data Streams instead of a fixed index.
        :type data_stream: ObservabilityPipelineOpenSearchDestinationDataStream, optional

        :param id: The unique identifier for this component.
        :type id: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param type: The destination type. The value should always be ``opensearch``.
        :type type: ObservabilityPipelineOpenSearchDestinationType
        """
        if bulk_index is not unset:
            kwargs["bulk_index"] = bulk_index
        if data_stream is not unset:
            kwargs["data_stream"] = data_stream
        super().__init__(kwargs)

        self_.id = id
        self_.inputs = inputs
        self_.type = type
