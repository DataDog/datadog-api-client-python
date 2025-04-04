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
    from datadog_api_client.v2.model.pipeline_rename_fields_processor_field import PipelineRenameFieldsProcessorField
    from datadog_api_client.v2.model.pipeline_rename_fields_processor_type import PipelineRenameFieldsProcessorType


class PipelineRenameFieldsProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.pipeline_rename_fields_processor_field import (
            PipelineRenameFieldsProcessorField,
        )
        from datadog_api_client.v2.model.pipeline_rename_fields_processor_type import PipelineRenameFieldsProcessorType

        return {
            "fields": ([PipelineRenameFieldsProcessorField],),
            "id": (str,),
            "include": (str,),
            "inputs": ([str],),
            "type": (PipelineRenameFieldsProcessorType,),
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
        fields: List[PipelineRenameFieldsProcessorField],
        id: str,
        include: str,
        inputs: List[str],
        type: PipelineRenameFieldsProcessorType,
        **kwargs,
    ):
        """
        The ``rename_fields`` processor changes field names.

        :param fields: A list of rename rules specifying which fields to rename in the event, what to rename them to, and whether to preserve the original fields.
        :type fields: [PipelineRenameFieldsProcessorField]

        :param id: A unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
        :type id: str

        :param include: A Datadog search query used to determine which logs this processor targets.
        :type include: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param type: The processor type. The value should always be ``rename_fields``.
        :type type: PipelineRenameFieldsProcessorType
        """
        super().__init__(kwargs)

        self_.fields = fields
        self_.id = id
        self_.include = include
        self_.inputs = inputs
        self_.type = type
