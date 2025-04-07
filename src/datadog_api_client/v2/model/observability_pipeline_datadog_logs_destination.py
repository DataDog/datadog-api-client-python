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
    from datadog_api_client.v2.model.observability_pipeline_datadog_logs_destination_type import (
        ObservabilityPipelineDatadogLogsDestinationType,
    )


class ObservabilityPipelineDatadogLogsDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_datadog_logs_destination_type import (
            ObservabilityPipelineDatadogLogsDestinationType,
        )

        return {
            "id": (str,),
            "inputs": ([str],),
            "type": (ObservabilityPipelineDatadogLogsDestinationType,),
        }

    attribute_map = {
        "id": "id",
        "inputs": "inputs",
        "type": "type",
    }

    def __init__(self_, id: str, inputs: List[str], type: ObservabilityPipelineDatadogLogsDestinationType, **kwargs):
        """
        The ``datadog_logs`` destination forwards logs to Datadog Log Management.

        :param id: The unique identifier for this component.
        :type id: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param type: The destination type. The value should always be ``datadog_logs``.
        :type type: ObservabilityPipelineDatadogLogsDestinationType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.inputs = inputs
        self_.type = type
