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
    from datadog_api_client.v2.model.observability_pipeline_elasticsearch_destination_type import (
        ObservabilityPipelineElasticsearchDestinationType,
    )


class ObservabilityPipelineElasticsearchDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_elasticsearch_destination_api_version import (
            ObservabilityPipelineElasticsearchDestinationApiVersion,
        )
        from datadog_api_client.v2.model.observability_pipeline_elasticsearch_destination_type import (
            ObservabilityPipelineElasticsearchDestinationType,
        )

        return {
            "api_version": (ObservabilityPipelineElasticsearchDestinationApiVersion,),
            "bulk_index": (str,),
            "id": (str,),
            "inputs": ([str],),
            "type": (ObservabilityPipelineElasticsearchDestinationType,),
        }

    attribute_map = {
        "api_version": "api_version",
        "bulk_index": "bulk_index",
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
        **kwargs,
    ):
        """
        The ``elasticsearch`` destination writes logs to an Elasticsearch cluster.

        :param api_version: The Elasticsearch API version to use. Set to ``auto`` to auto-detect.
        :type api_version: ObservabilityPipelineElasticsearchDestinationApiVersion, optional

        :param bulk_index: The index to write logs to in Elasticsearch.
        :type bulk_index: str, optional

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
        super().__init__(kwargs)

        self_.id = id
        self_.inputs = inputs
        self_.type = type
