# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_sentinel_one_destination_region import (
        ObservabilityPipelineSentinelOneDestinationRegion,
    )
    from datadog_api_client.v2.model.observability_pipeline_sentinel_one_destination_type import (
        ObservabilityPipelineSentinelOneDestinationType,
    )


class ObservabilityPipelineSentinelOneDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_sentinel_one_destination_region import (
            ObservabilityPipelineSentinelOneDestinationRegion,
        )
        from datadog_api_client.v2.model.observability_pipeline_sentinel_one_destination_type import (
            ObservabilityPipelineSentinelOneDestinationType,
        )

        return {
            "id": (str,),
            "inputs": ([str],),
            "region": (ObservabilityPipelineSentinelOneDestinationRegion,),
            "type": (ObservabilityPipelineSentinelOneDestinationType,),
        }

    attribute_map = {
        "id": "id",
        "inputs": "inputs",
        "region": "region",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        inputs: List[str],
        region: ObservabilityPipelineSentinelOneDestinationRegion,
        type: ObservabilityPipelineSentinelOneDestinationType,
        **kwargs,
    ):
        """
        The ``sentinel_one`` destination sends logs to SentinelOne.

        :param id: The unique identifier for this component.
        :type id: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param region: The SentinelOne region to send logs to.
        :type region: ObservabilityPipelineSentinelOneDestinationRegion

        :param type: The destination type. The value should always be ``sentinel_one``.
        :type type: ObservabilityPipelineSentinelOneDestinationType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.inputs = inputs
        self_.region = region
        self_.type = type
