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
    from datadog_api_client.v2.model.observability_pipeline_split_array_processor_array_config import (
        ObservabilityPipelineSplitArrayProcessorArrayConfig,
    )
    from datadog_api_client.v2.model.observability_pipeline_split_array_processor_type import (
        ObservabilityPipelineSplitArrayProcessorType,
    )


class ObservabilityPipelineSplitArrayProcessor(ModelNormal):
    validations = {
        "arrays": {
            "max_items": 15,
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_split_array_processor_array_config import (
            ObservabilityPipelineSplitArrayProcessorArrayConfig,
        )
        from datadog_api_client.v2.model.observability_pipeline_split_array_processor_type import (
            ObservabilityPipelineSplitArrayProcessorType,
        )

        return {
            "arrays": ([ObservabilityPipelineSplitArrayProcessorArrayConfig],),
            "display_name": (str,),
            "enabled": (bool,),
            "id": (str,),
            "include": (str,),
            "type": (ObservabilityPipelineSplitArrayProcessorType,),
        }

    attribute_map = {
        "arrays": "arrays",
        "display_name": "display_name",
        "enabled": "enabled",
        "id": "id",
        "include": "include",
        "type": "type",
    }

    def __init__(
        self_,
        arrays: List[ObservabilityPipelineSplitArrayProcessorArrayConfig],
        enabled: bool,
        id: str,
        include: str,
        type: ObservabilityPipelineSplitArrayProcessorType,
        display_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``split_array`` processor splits array fields into separate events based on configured rules.

        **Supported pipeline types:** logs

        :param arrays: A list of array split configurations.
        :type arrays: [ObservabilityPipelineSplitArrayProcessorArrayConfig]

        :param display_name: The display name for a component.
        :type display_name: str, optional

        :param enabled: Whether this processor is enabled.
        :type enabled: bool

        :param id: The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the ``input`` to downstream components).
        :type id: str

        :param include: A Datadog search query used to determine which logs this processor targets. For split_array, this should typically be ``*``.
        :type include: str

        :param type: The processor type. The value should always be ``split_array``.
        :type type: ObservabilityPipelineSplitArrayProcessorType
        """
        if display_name is not unset:
            kwargs["display_name"] = display_name
        super().__init__(kwargs)

        self_.arrays = arrays
        self_.enabled = enabled
        self_.id = id
        self_.include = include
        self_.type = type
