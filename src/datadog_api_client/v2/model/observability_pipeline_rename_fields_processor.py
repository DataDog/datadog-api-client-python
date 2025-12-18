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
    from datadog_api_client.v2.model.observability_pipeline_rename_fields_processor_field import (
        ObservabilityPipelineRenameFieldsProcessorField,
    )
    from datadog_api_client.v2.model.observability_pipeline_rename_fields_processor_type import (
        ObservabilityPipelineRenameFieldsProcessorType,
    )


class ObservabilityPipelineRenameFieldsProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_rename_fields_processor_field import (
            ObservabilityPipelineRenameFieldsProcessorField,
        )
        from datadog_api_client.v2.model.observability_pipeline_rename_fields_processor_type import (
            ObservabilityPipelineRenameFieldsProcessorType,
        )

        return {
            "display_name": (str,),
            "enabled": (bool,),
            "fields": ([ObservabilityPipelineRenameFieldsProcessorField],),
            "id": (str,),
            "include": (str,),
            "type": (ObservabilityPipelineRenameFieldsProcessorType,),
        }

    attribute_map = {
        "display_name": "display_name",
        "enabled": "enabled",
        "fields": "fields",
        "id": "id",
        "include": "include",
        "type": "type",
    }

    def __init__(
        self_,
        enabled: bool,
        fields: List[ObservabilityPipelineRenameFieldsProcessorField],
        id: str,
        include: str,
        type: ObservabilityPipelineRenameFieldsProcessorType,
        display_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``rename_fields`` processor changes field names.

        :param display_name: The display name for a component.
        :type display_name: str, optional

        :param enabled: Whether this processor is enabled.
        :type enabled: bool

        :param fields: A list of rename rules specifying which fields to rename in the event, what to rename them to, and whether to preserve the original fields.
        :type fields: [ObservabilityPipelineRenameFieldsProcessorField]

        :param id: A unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
        :type id: str

        :param include: A Datadog search query used to determine which logs this processor targets.
        :type include: str

        :param type: The processor type. The value should always be ``rename_fields``.
        :type type: ObservabilityPipelineRenameFieldsProcessorType
        """
        if display_name is not unset:
            kwargs["display_name"] = display_name
        super().__init__(kwargs)

        self_.enabled = enabled
        self_.fields = fields
        self_.id = id
        self_.include = include
        self_.type = type
