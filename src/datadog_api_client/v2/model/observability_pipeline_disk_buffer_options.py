# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_buffer_options_disk_type import (
        ObservabilityPipelineBufferOptionsDiskType,
    )


class ObservabilityPipelineDiskBufferOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_buffer_options_disk_type import (
            ObservabilityPipelineBufferOptionsDiskType,
        )

        return {
            "max_size": (int,),
            "type": (ObservabilityPipelineBufferOptionsDiskType,),
        }

    attribute_map = {
        "max_size": "max_size",
        "type": "type",
    }

    def __init__(
        self_,
        max_size: Union[int, UnsetType] = unset,
        type: Union[ObservabilityPipelineBufferOptionsDiskType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Options for configuring a disk buffer.

        :param max_size: Maximum size of the disk buffer.
        :type max_size: int, optional

        :param type: Specifies the buffer type to configure. This option supports only a disk buffer.
        :type type: ObservabilityPipelineBufferOptionsDiskType, optional
        """
        if max_size is not unset:
            kwargs["max_size"] = max_size
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
