# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_azure_data_explorer_destination_auth import (
        ObservabilityPipelineAzureDataExplorerDestinationAuth,
    )
    from datadog_api_client.v2.model.observability_pipeline_azure_data_explorer_destination_batch import (
        ObservabilityPipelineAzureDataExplorerDestinationBatch,
    )
    from datadog_api_client.v2.model.observability_pipeline_buffer_options import ObservabilityPipelineBufferOptions
    from datadog_api_client.v2.model.observability_pipeline_azure_storage_destination_compression_gzip import (
        ObservabilityPipelineAzureStorageDestinationCompressionGzip,
    )
    from datadog_api_client.v2.model.observability_pipeline_azure_data_explorer_destination_type import (
        ObservabilityPipelineAzureDataExplorerDestinationType,
    )
    from datadog_api_client.v2.model.observability_pipeline_azure_data_explorer_destination_auth_azure_cli import (
        ObservabilityPipelineAzureDataExplorerDestinationAuthAzureCli,
    )
    from datadog_api_client.v2.model.observability_pipeline_azure_data_explorer_destination_auth_client_secret import (
        ObservabilityPipelineAzureDataExplorerDestinationAuthClientSecret,
    )
    from datadog_api_client.v2.model.observability_pipeline_azure_data_explorer_destination_auth_client_certificate import (
        ObservabilityPipelineAzureDataExplorerDestinationAuthClientCertificate,
    )
    from datadog_api_client.v2.model.observability_pipeline_azure_data_explorer_destination_auth_managed_identity import (
        ObservabilityPipelineAzureDataExplorerDestinationAuthManagedIdentity,
    )
    from datadog_api_client.v2.model.observability_pipeline_azure_data_explorer_destination_auth_managed_identity_client_assertion import (
        ObservabilityPipelineAzureDataExplorerDestinationAuthManagedIdentityClientAssertion,
    )
    from datadog_api_client.v2.model.observability_pipeline_azure_data_explorer_destination_auth_workload_identity import (
        ObservabilityPipelineAzureDataExplorerDestinationAuthWorkloadIdentity,
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


class ObservabilityPipelineAzureDataExplorerDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_azure_data_explorer_destination_auth import (
            ObservabilityPipelineAzureDataExplorerDestinationAuth,
        )
        from datadog_api_client.v2.model.observability_pipeline_azure_data_explorer_destination_batch import (
            ObservabilityPipelineAzureDataExplorerDestinationBatch,
        )
        from datadog_api_client.v2.model.observability_pipeline_buffer_options import ObservabilityPipelineBufferOptions
        from datadog_api_client.v2.model.observability_pipeline_azure_storage_destination_compression_gzip import (
            ObservabilityPipelineAzureStorageDestinationCompressionGzip,
        )
        from datadog_api_client.v2.model.observability_pipeline_azure_data_explorer_destination_type import (
            ObservabilityPipelineAzureDataExplorerDestinationType,
        )

        return {
            "auth": (ObservabilityPipelineAzureDataExplorerDestinationAuth,),
            "batch": (ObservabilityPipelineAzureDataExplorerDestinationBatch,),
            "buffer": (ObservabilityPipelineBufferOptions,),
            "compression": (ObservabilityPipelineAzureStorageDestinationCompressionGzip,),
            "database": (str,),
            "id": (str,),
            "ingestion_endpoint_key": (str,),
            "inputs": ([str],),
            "mapping_reference": (str, none_type),
            "table": (str,),
            "token_scope": (str,),
            "type": (ObservabilityPipelineAzureDataExplorerDestinationType,),
        }

    attribute_map = {
        "auth": "auth",
        "batch": "batch",
        "buffer": "buffer",
        "compression": "compression",
        "database": "database",
        "id": "id",
        "ingestion_endpoint_key": "ingestion_endpoint_key",
        "inputs": "inputs",
        "mapping_reference": "mapping_reference",
        "table": "table",
        "token_scope": "token_scope",
        "type": "type",
    }

    def __init__(
        self_,
        auth: Union[
            ObservabilityPipelineAzureDataExplorerDestinationAuth,
            ObservabilityPipelineAzureDataExplorerDestinationAuthAzureCli,
            ObservabilityPipelineAzureDataExplorerDestinationAuthClientSecret,
            ObservabilityPipelineAzureDataExplorerDestinationAuthClientCertificate,
            ObservabilityPipelineAzureDataExplorerDestinationAuthManagedIdentity,
            ObservabilityPipelineAzureDataExplorerDestinationAuthManagedIdentityClientAssertion,
            ObservabilityPipelineAzureDataExplorerDestinationAuthWorkloadIdentity,
        ],
        database: str,
        id: str,
        inputs: List[str],
        table: str,
        type: ObservabilityPipelineAzureDataExplorerDestinationType,
        batch: Union[ObservabilityPipelineAzureDataExplorerDestinationBatch, UnsetType] = unset,
        buffer: Union[
            ObservabilityPipelineBufferOptions,
            ObservabilityPipelineDiskBufferOptions,
            ObservabilityPipelineMemoryBufferOptions,
            ObservabilityPipelineMemoryBufferSizeOptions,
            UnsetType,
        ] = unset,
        compression: Union[ObservabilityPipelineAzureStorageDestinationCompressionGzip, UnsetType] = unset,
        ingestion_endpoint_key: Union[str, UnsetType] = unset,
        mapping_reference: Union[str, none_type, UnsetType] = unset,
        token_scope: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``azure_data_explorer`` destination sends log events to an Azure Data Explorer table.

        **Supported pipeline types:** logs

        :param auth: Authentication configuration for Azure Data Explorer. The ``azure_credential_kind`` field selects the credential type.
        :type auth: ObservabilityPipelineAzureDataExplorerDestinationAuth

        :param batch: Event batching settings for Azure Data Explorer ingestion.
        :type batch: ObservabilityPipelineAzureDataExplorerDestinationBatch, optional

        :param buffer: Configuration for buffer settings on destination components.
        :type buffer: ObservabilityPipelineBufferOptions, optional

        :param compression: Gzip compression.
        :type compression: ObservabilityPipelineAzureStorageDestinationCompressionGzip, optional

        :param database: The name of the Azure Data Explorer database to ingest into. Supports template syntax.
        :type database: str

        :param id: The unique identifier for this component.
        :type id: str

        :param ingestion_endpoint_key: Name of the environment variable or secret that holds the Azure Data Explorer ingestion endpoint URL.
            Defaults to ``DESTINATION_AZURE_DATA_EXPLORER_INGESTION_ENDPOINT`` (prefixed with ``DD_OP_`` at runtime).
        :type ingestion_endpoint_key: str, optional

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param mapping_reference: The name of a pre-created ingestion mapping on the table used to map incoming events to columns. Supports template syntax.
        :type mapping_reference: str, none_type, optional

        :param table: The name of the Azure Data Explorer table to ingest into. Supports template syntax.
        :type table: str

        :param token_scope: The OAuth scope requested when acquiring an access token for Azure Data Explorer.
            Defaults to ``https://kusto.kusto.windows.net/.default``.
        :type token_scope: str, optional

        :param type: The destination type. The value should always be ``azure_data_explorer``.
        :type type: ObservabilityPipelineAzureDataExplorerDestinationType
        """
        if batch is not unset:
            kwargs["batch"] = batch
        if buffer is not unset:
            kwargs["buffer"] = buffer
        if compression is not unset:
            kwargs["compression"] = compression
        if ingestion_endpoint_key is not unset:
            kwargs["ingestion_endpoint_key"] = ingestion_endpoint_key
        if mapping_reference is not unset:
            kwargs["mapping_reference"] = mapping_reference
        if token_scope is not unset:
            kwargs["token_scope"] = token_scope
        super().__init__(kwargs)

        self_.auth = auth
        self_.database = database
        self_.id = id
        self_.inputs = inputs
        self_.table = table
        self_.type = type
