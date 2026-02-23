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
    from datadog_api_client.v2.model.microsoft_sentinel_destination_type import MicrosoftSentinelDestinationType
    from datadog_api_client.v2.model.observability_pipeline_disk_buffer_options import (
        ObservabilityPipelineDiskBufferOptions,
    )
    from datadog_api_client.v2.model.observability_pipeline_memory_buffer_options import (
        ObservabilityPipelineMemoryBufferOptions,
    )
    from datadog_api_client.v2.model.observability_pipeline_memory_buffer_size_options import (
        ObservabilityPipelineMemoryBufferSizeOptions,
    )


class MicrosoftSentinelDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_buffer_options import ObservabilityPipelineBufferOptions
        from datadog_api_client.v2.model.microsoft_sentinel_destination_type import MicrosoftSentinelDestinationType

        return {
            "buffer": (ObservabilityPipelineBufferOptions,),
            "client_id": (str,),
            "client_secret_key": (str,),
            "dce_uri_key": (str,),
            "dcr_immutable_id": (str,),
            "id": (str,),
            "inputs": ([str],),
            "table": (str,),
            "tenant_id": (str,),
            "type": (MicrosoftSentinelDestinationType,),
        }

    attribute_map = {
        "buffer": "buffer",
        "client_id": "client_id",
        "client_secret_key": "client_secret_key",
        "dce_uri_key": "dce_uri_key",
        "dcr_immutable_id": "dcr_immutable_id",
        "id": "id",
        "inputs": "inputs",
        "table": "table",
        "tenant_id": "tenant_id",
        "type": "type",
    }

    def __init__(
        self_,
        client_id: str,
        dcr_immutable_id: str,
        id: str,
        inputs: List[str],
        table: str,
        tenant_id: str,
        type: MicrosoftSentinelDestinationType,
        buffer: Union[
            ObservabilityPipelineBufferOptions,
            ObservabilityPipelineDiskBufferOptions,
            ObservabilityPipelineMemoryBufferOptions,
            ObservabilityPipelineMemoryBufferSizeOptions,
            UnsetType,
        ] = unset,
        client_secret_key: Union[str, UnsetType] = unset,
        dce_uri_key: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``microsoft_sentinel`` destination forwards logs to Microsoft Sentinel.

        **Supported pipeline types:** logs

        :param buffer: Configuration for buffer settings on destination components.
        :type buffer: ObservabilityPipelineBufferOptions, optional

        :param client_id: Azure AD client ID used for authentication.
        :type client_id: str

        :param client_secret_key: Name of the environment variable or secret that holds the Azure AD client secret.
        :type client_secret_key: str, optional

        :param dce_uri_key: Name of the environment variable or secret that holds the Data Collection Endpoint (DCE) URI.
        :type dce_uri_key: str, optional

        :param dcr_immutable_id: The immutable ID of the Data Collection Rule (DCR).
        :type dcr_immutable_id: str

        :param id: The unique identifier for this component.
        :type id: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param table: The name of the Log Analytics table where logs are sent.
        :type table: str

        :param tenant_id: Azure AD tenant ID.
        :type tenant_id: str

        :param type: The destination type. The value should always be ``microsoft_sentinel``.
        :type type: MicrosoftSentinelDestinationType
        """
        if buffer is not unset:
            kwargs["buffer"] = buffer
        if client_secret_key is not unset:
            kwargs["client_secret_key"] = client_secret_key
        if dce_uri_key is not unset:
            kwargs["dce_uri_key"] = dce_uri_key
        super().__init__(kwargs)

        self_.client_id = client_id
        self_.dcr_immutable_id = dcr_immutable_id
        self_.id = id
        self_.inputs = inputs
        self_.table = table
        self_.tenant_id = tenant_id
        self_.type = type
