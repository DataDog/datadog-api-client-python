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
    from datadog_api_client.v2.model.observability_pipeline_sumo_logic_source_type import (
        ObservabilityPipelineSumoLogicSourceType,
    )


class ObservabilityPipelineSumoLogicSource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_sumo_logic_source_type import (
            ObservabilityPipelineSumoLogicSourceType,
        )

        return {
            "id": (str,),
            "type": (ObservabilityPipelineSumoLogicSourceType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: ObservabilityPipelineSumoLogicSourceType, **kwargs):
        """
        The ``sumo_logic`` source receives logs from Sumo Logic collectors.

        :param id: The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
        :type id: str

        :param type: The source type. The value should always be ``sumo_logic``.
        :type type: ObservabilityPipelineSumoLogicSourceType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
