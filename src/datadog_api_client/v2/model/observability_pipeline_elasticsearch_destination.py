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
    from datadog_api_client.v2.model.observability_pipeline_elasticsearch_destination_api_version import (
        ObservabilityPipelineElasticsearchDestinationApiVersion,
    )
    from datadog_api_client.v2.model.observability_pipeline_elasticsearch_destination_data_stream import (
        ObservabilityPipelineElasticsearchDestinationDataStream,
    )
    from datadog_api_client.v2.model.observability_pipeline_elasticsearch_destination_type import (
        ObservabilityPipelineElasticsearchDestinationType,
    )


class ObservabilityPipelineElasticsearchDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_elasticsearch_destination_api_version import (
            ObservabilityPipelineElasticsearchDestinationApiVersion,
        )
        from datadog_api_client.v2.model.observability_pipeline_elasticsearch_destination_data_stream import (
            ObservabilityPipelineElasticsearchDestinationDataStream,
        )
        from datadog_api_client.v2.model.observability_pipeline_elasticsearch_destination_type import (
            ObservabilityPipelineElasticsearchDestinationType,
        )

        return {
            "api_version": (ObservabilityPipelineElasticsearchDestinationApiVersion,),
            "bulk_index": (str,),
            "data_stream": (ObservabilityPipelineElasticsearchDestinationDataStream,),
            "id": (str,),
            "inputs": ([str],),
            "type": (ObservabilityPipelineElasticsearchDestinationType,),
        }

    attribute_map = {
        "api_version": "api_version",
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
        type: ObservabilityPipelineElasticsearchDestinationType,
        api_version: Union[ObservabilityPipelineElasticsearchDestinationApiVersion, UnsetType] = unset,
        bulk_index: Union[str, UnsetType] = unset,
        data_stream: Union[ObservabilityPipelineElasticsearchDestinationDataStream, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``elasticsearch`` destination writes logs to an Elasticsearch cluster.

        :param api_version: The Elasticsearch API version to use. Set to ``auto`` to auto-detect.
        :type api_version: ObservabilityPipelineElasticsearchDestinationApiVersion, optional

        :param bulk_index: The index to write logs to in Elasticsearch.
        :type bulk_index: str, optional

        :param data_stream: Configuration options for writing to Elasticsearch Data Streams instead of a fixed index.
        :type data_stream: ObservabilityPipelineElasticsearchDestinationDataStream, optional

        :param id: The unique identifier for this component.
        :type id: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param type: The destination type. The value should always be ``elasticsearch``.
        :type type: ObservabilityPipelineElasticsearchDestinationType
        """
        if api_version is not unset:
            kwargs["api_version"] = api_version
        if bulk_index is not unset:
            kwargs["bulk_index"] = bulk_index
        if data_stream is not unset:
            kwargs["data_stream"] = data_stream
        super().__init__(kwargs)

        self_.id = id
        self_.inputs = inputs
        self_.type = type
