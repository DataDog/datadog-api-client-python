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
    from datadog_api_client.v2.model.observability_pipeline_new_relic_destination_region import (
        ObservabilityPipelineNewRelicDestinationRegion,
    )
    from datadog_api_client.v2.model.observability_pipeline_new_relic_destination_type import (
        ObservabilityPipelineNewRelicDestinationType,
    )


class ObservabilityPipelineNewRelicDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_new_relic_destination_region import (
            ObservabilityPipelineNewRelicDestinationRegion,
        )
        from datadog_api_client.v2.model.observability_pipeline_new_relic_destination_type import (
            ObservabilityPipelineNewRelicDestinationType,
        )

        return {
            "id": (str,),
            "inputs": ([str],),
            "region": (ObservabilityPipelineNewRelicDestinationRegion,),
            "type": (ObservabilityPipelineNewRelicDestinationType,),
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
        region: ObservabilityPipelineNewRelicDestinationRegion,
        type: ObservabilityPipelineNewRelicDestinationType,
        **kwargs,
    ):
        """
        The ``new_relic`` destination sends logs to the New Relic platform.

        :param id: The unique identifier for this component.
        :type id: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param region: The New Relic region.
        :type region: ObservabilityPipelineNewRelicDestinationRegion

        :param type: The destination type. The value should always be ``new_relic``.
        :type type: ObservabilityPipelineNewRelicDestinationType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.inputs = inputs
        self_.region = region
        self_.type = type
