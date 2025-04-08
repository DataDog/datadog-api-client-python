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
    from datadog_api_client.v2.model.observability_pipeline_field_value import ObservabilityPipelineFieldValue
    from datadog_api_client.v2.model.observability_pipeline_add_fields_processor_type import (
        ObservabilityPipelineAddFieldsProcessorType,
    )


class ObservabilityPipelineAddFieldsProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_field_value import ObservabilityPipelineFieldValue
        from datadog_api_client.v2.model.observability_pipeline_add_fields_processor_type import (
            ObservabilityPipelineAddFieldsProcessorType,
        )

        return {
            "fields": ([ObservabilityPipelineFieldValue],),
            "id": (str,),
            "include": (str,),
            "inputs": ([str],),
            "type": (ObservabilityPipelineAddFieldsProcessorType,),
        }

    attribute_map = {
        "fields": "fields",
        "id": "id",
        "include": "include",
        "inputs": "inputs",
        "type": "type",
    }

    def __init__(
        self_,
        fields: List[ObservabilityPipelineFieldValue],
        id: str,
        include: str,
        inputs: List[str],
        type: ObservabilityPipelineAddFieldsProcessorType,
        **kwargs,
    ):
        """
        The ``add_fields`` processor adds static key-value fields to logs.

        :param fields: A list of static fields (key-value pairs) that is added to each log event processed by this component.
        :type fields: [ObservabilityPipelineFieldValue]

        :param id: The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the ``input`` to downstream components).
        :type id: str

        :param include: A Datadog search query used to determine which logs this processor targets.
        :type include: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param type: The processor type. The value should always be ``add_fields``.
        :type type: ObservabilityPipelineAddFieldsProcessorType
        """
        super().__init__(kwargs)

        self_.fields = fields
        self_.id = id
        self_.include = include
        self_.inputs = inputs
        self_.type = type
