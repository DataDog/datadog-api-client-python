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
    from datadog_api_client.v2.model.observability_pipeline_buffer_options import ObservabilityPipelineBufferOptions
    from datadog_api_client.v2.model.observability_pipeline_new_relic_destination_region import (
        ObservabilityPipelineNewRelicDestinationRegion,
    )
    from datadog_api_client.v2.model.observability_pipeline_new_relic_destination_type import (
        ObservabilityPipelineNewRelicDestinationType,
    )
    from datadog_api_client.v2.model.observability_pipeline_disk_buffer_options import (
        ObservabilityPipelineDiskBufferOptions,
    )
    from datadog_api_client.v2.model.observability_pipeline_memory_buffer_options import (
        ObservabilityPipelineMemoryBufferOptions,
    )
    from datadog_api_client.v2.model.observability_pipeline_memory_buffer_size_options import (
        ObservabilityPipelineMemoryBufferSizeOptions,
    )


class ObservabilityPipelineNewRelicDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_buffer_options import ObservabilityPipelineBufferOptions
        from datadog_api_client.v2.model.observability_pipeline_new_relic_destination_region import (
            ObservabilityPipelineNewRelicDestinationRegion,
        )
        from datadog_api_client.v2.model.observability_pipeline_new_relic_destination_type import (
            ObservabilityPipelineNewRelicDestinationType,
        )

        return {
            "account_id_key": (str,),
            "buffer": (ObservabilityPipelineBufferOptions,),
            "id": (str,),
            "inputs": ([str],),
            "license_key_key": (str,),
            "region": (ObservabilityPipelineNewRelicDestinationRegion,),
            "type": (ObservabilityPipelineNewRelicDestinationType,),
        }

    attribute_map = {
        "account_id_key": "account_id_key",
        "buffer": "buffer",
        "id": "id",
        "inputs": "inputs",
        "license_key_key": "license_key_key",
        "region": "region",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        inputs: List[str],
        region: ObservabilityPipelineNewRelicDestinationRegion,
        type: ObservabilityPipelineNewRelicDestinationType,
        account_id_key: Union[str, UnsetType] = unset,
        buffer: Union[
            ObservabilityPipelineBufferOptions,
            ObservabilityPipelineDiskBufferOptions,
            ObservabilityPipelineMemoryBufferOptions,
            ObservabilityPipelineMemoryBufferSizeOptions,
            UnsetType,
        ] = unset,
        license_key_key: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``new_relic`` destination sends logs to the New Relic platform.

        **Supported pipeline types:** logs

        :param account_id_key: Name of the environment variable or secret that holds the New Relic account ID.
        :type account_id_key: str, optional

        :param buffer: Configuration for buffer settings on destination components.
        :type buffer: ObservabilityPipelineBufferOptions, optional

        :param id: The unique identifier for this component.
        :type id: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param license_key_key: Name of the environment variable or secret that holds the New Relic license key.
        :type license_key_key: str, optional

        :param region: The New Relic region.
        :type region: ObservabilityPipelineNewRelicDestinationRegion

        :param type: The destination type. The value should always be ``new_relic``.
        :type type: ObservabilityPipelineNewRelicDestinationType
        """
        if account_id_key is not unset:
            kwargs["account_id_key"] = account_id_key
        if buffer is not unset:
            kwargs["buffer"] = buffer
        if license_key_key is not unset:
            kwargs["license_key_key"] = license_key_key
        super().__init__(kwargs)

        self_.id = id
        self_.inputs = inputs
        self_.region = region
        self_.type = type
