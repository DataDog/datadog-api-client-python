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
    from datadog_api_client.v2.model.observability_pipeline_databricks_zerobus_destination_auth import (
        ObservabilityPipelineDatabricksZerobusDestinationAuth,
    )
    from datadog_api_client.v2.model.observability_pipeline_buffer_options import ObservabilityPipelineBufferOptions
    from datadog_api_client.v2.model.observability_pipeline_databricks_zerobus_destination_type import (
        ObservabilityPipelineDatabricksZerobusDestinationType,
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


class ObservabilityPipelineDatabricksZerobusDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_databricks_zerobus_destination_auth import (
            ObservabilityPipelineDatabricksZerobusDestinationAuth,
        )
        from datadog_api_client.v2.model.observability_pipeline_buffer_options import ObservabilityPipelineBufferOptions
        from datadog_api_client.v2.model.observability_pipeline_databricks_zerobus_destination_type import (
            ObservabilityPipelineDatabricksZerobusDestinationType,
        )

        return {
            "auth": (ObservabilityPipelineDatabricksZerobusDestinationAuth,),
            "buffer": (ObservabilityPipelineBufferOptions,),
            "id": (str,),
            "ingestion_endpoint": (str,),
            "inputs": ([str],),
            "table_name": (str,),
            "type": (ObservabilityPipelineDatabricksZerobusDestinationType,),
            "unity_catalog_endpoint": (str,),
        }

    attribute_map = {
        "auth": "auth",
        "buffer": "buffer",
        "id": "id",
        "ingestion_endpoint": "ingestion_endpoint",
        "inputs": "inputs",
        "table_name": "table_name",
        "type": "type",
        "unity_catalog_endpoint": "unity_catalog_endpoint",
    }

    def __init__(
        self_,
        auth: ObservabilityPipelineDatabricksZerobusDestinationAuth,
        id: str,
        ingestion_endpoint: str,
        inputs: List[str],
        table_name: str,
        type: ObservabilityPipelineDatabricksZerobusDestinationType,
        unity_catalog_endpoint: str,
        buffer: Union[
            ObservabilityPipelineBufferOptions,
            ObservabilityPipelineDiskBufferOptions,
            ObservabilityPipelineMemoryBufferOptions,
            ObservabilityPipelineMemoryBufferSizeOptions,
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """
        The ``databricks_zerobus`` destination sends logs to Databricks using the Zerobus ingestion API, streaming data directly into your Databricks Lakehouse.

        **Supported pipeline types:** Logs, rehydration

        :param auth: OAuth credentials for authenticating with the Databricks Zerobus ingestion API.
        :type auth: ObservabilityPipelineDatabricksZerobusDestinationAuth

        :param buffer: Configuration for buffer settings on destination components.
        :type buffer: ObservabilityPipelineBufferOptions, optional

        :param id: The unique identifier for this component.
        :type id: str

        :param ingestion_endpoint: Your Databricks Zerobus ingestion endpoint. This is the endpoint used to stream data directly into your Databricks Lakehouse.
        :type ingestion_endpoint: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param table_name: The fully qualified name of your target Databricks table. Make sure this table already exists in your Databricks workspace before deploying.
        :type table_name: str

        :param type: The destination type. The value must be ``databricks_zerobus``.
        :type type: ObservabilityPipelineDatabricksZerobusDestinationType

        :param unity_catalog_endpoint: Your Databricks workspace URL. This is used to communicate with the Unity Catalog API.
        :type unity_catalog_endpoint: str
        """
        if buffer is not unset:
            kwargs["buffer"] = buffer
        super().__init__(kwargs)

        self_.auth = auth
        self_.id = id
        self_.ingestion_endpoint = ingestion_endpoint
        self_.inputs = inputs
        self_.table_name = table_name
        self_.type = type
        self_.unity_catalog_endpoint = unity_catalog_endpoint
