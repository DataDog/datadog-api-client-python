# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class ObservabilityPipelineConfigDestinationItem(ModelComposed):
    def __init__(self, **kwargs):
        """
        A destination for the pipeline.

        :param id: The unique identifier for this component.
        :type id: str

        :param inputs: A list of component IDs whose output is used as the `input` for this component.
        :type inputs: [str]

        :param type: The destination type. The value should always be `datadog_logs`.
        :type type: ObservabilityPipelineDatadogLogsDestinationType
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.observability_pipeline_datadog_logs_destination import (
            ObservabilityPipelineDatadogLogsDestination,
        )

        return {
            "oneOf": [
                ObservabilityPipelineDatadogLogsDestination,
            ],
        }
