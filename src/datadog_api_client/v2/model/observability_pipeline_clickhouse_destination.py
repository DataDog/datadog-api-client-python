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
    from datadog_api_client.v2.model.observability_pipeline_clickhouse_destination_auth import (
        ObservabilityPipelineClickhouseDestinationAuth,
    )
    from datadog_api_client.v2.model.observability_pipeline_clickhouse_destination_batch import (
        ObservabilityPipelineClickhouseDestinationBatch,
    )
    from datadog_api_client.v2.model.observability_pipeline_clickhouse_destination_batch_encoding import (
        ObservabilityPipelineClickhouseDestinationBatchEncoding,
    )
    from datadog_api_client.v2.model.observability_pipeline_clickhouse_destination_compression import (
        ObservabilityPipelineClickhouseDestinationCompression,
    )
    from datadog_api_client.v2.model.observability_pipeline_clickhouse_destination_format import (
        ObservabilityPipelineClickhouseDestinationFormat,
    )
    from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
    from datadog_api_client.v2.model.observability_pipeline_clickhouse_destination_type import (
        ObservabilityPipelineClickhouseDestinationType,
    )
    from datadog_api_client.v2.model.observability_pipeline_clickhouse_destination_compression_object import (
        ObservabilityPipelineClickhouseDestinationCompressionObject,
    )


class ObservabilityPipelineClickhouseDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_clickhouse_destination_auth import (
            ObservabilityPipelineClickhouseDestinationAuth,
        )
        from datadog_api_client.v2.model.observability_pipeline_clickhouse_destination_batch import (
            ObservabilityPipelineClickhouseDestinationBatch,
        )
        from datadog_api_client.v2.model.observability_pipeline_clickhouse_destination_batch_encoding import (
            ObservabilityPipelineClickhouseDestinationBatchEncoding,
        )
        from datadog_api_client.v2.model.observability_pipeline_clickhouse_destination_compression import (
            ObservabilityPipelineClickhouseDestinationCompression,
        )
        from datadog_api_client.v2.model.observability_pipeline_clickhouse_destination_format import (
            ObservabilityPipelineClickhouseDestinationFormat,
        )
        from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
        from datadog_api_client.v2.model.observability_pipeline_clickhouse_destination_type import (
            ObservabilityPipelineClickhouseDestinationType,
        )

        return {
            "auth": (ObservabilityPipelineClickhouseDestinationAuth,),
            "batch": (ObservabilityPipelineClickhouseDestinationBatch,),
            "batch_encoding": (ObservabilityPipelineClickhouseDestinationBatchEncoding,),
            "compression": (ObservabilityPipelineClickhouseDestinationCompression,),
            "database": (str,),
            "date_time_best_effort": (bool,),
            "endpoint_url_key": (str,),
            "format": (ObservabilityPipelineClickhouseDestinationFormat,),
            "id": (str,),
            "inputs": ([str],),
            "skip_unknown_fields": (bool, none_type),
            "table": (str,),
            "tls": (ObservabilityPipelineTls,),
            "type": (ObservabilityPipelineClickhouseDestinationType,),
        }

    attribute_map = {
        "auth": "auth",
        "batch": "batch",
        "batch_encoding": "batch_encoding",
        "compression": "compression",
        "database": "database",
        "date_time_best_effort": "date_time_best_effort",
        "endpoint_url_key": "endpoint_url_key",
        "format": "format",
        "id": "id",
        "inputs": "inputs",
        "skip_unknown_fields": "skip_unknown_fields",
        "table": "table",
        "tls": "tls",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        inputs: List[str],
        table: str,
        type: ObservabilityPipelineClickhouseDestinationType,
        auth: Union[ObservabilityPipelineClickhouseDestinationAuth, UnsetType] = unset,
        batch: Union[ObservabilityPipelineClickhouseDestinationBatch, UnsetType] = unset,
        batch_encoding: Union[ObservabilityPipelineClickhouseDestinationBatchEncoding, UnsetType] = unset,
        compression: Union[
            ObservabilityPipelineClickhouseDestinationCompression,
            str,
            ObservabilityPipelineClickhouseDestinationCompressionObject,
            UnsetType,
        ] = unset,
        database: Union[str, UnsetType] = unset,
        date_time_best_effort: Union[bool, UnsetType] = unset,
        endpoint_url_key: Union[str, UnsetType] = unset,
        format: Union[ObservabilityPipelineClickhouseDestinationFormat, UnsetType] = unset,
        skip_unknown_fields: Union[bool, none_type, UnsetType] = unset,
        tls: Union[ObservabilityPipelineTls, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``clickhouse`` destination sends log events to a ClickHouse database table over HTTP.

        **Supported pipeline types:** logs.

        :param auth: HTTP Basic Authentication credentials for the ClickHouse destination.
            When ``strategy`` is ``basic`` , provide ``username_key`` and ``password_key`` that reference environment variables or secrets containing the credentials.
        :type auth: ObservabilityPipelineClickhouseDestinationAuth, optional

        :param batch: Batching configuration for ClickHouse inserts.
        :type batch: ObservabilityPipelineClickhouseDestinationBatch, optional

        :param batch_encoding: Batch encoding configuration for the ClickHouse destination.
            Required when ``format`` is ``arrow_stream``. The ``codec`` field must be set to ``arrow_stream``.
        :type batch_encoding: ObservabilityPipelineClickhouseDestinationBatchEncoding, optional

        :param compression: Compression setting for outbound HTTP requests to ClickHouse.
            Can be specified as a shorthand string ( ``"gzip"`` or ``"none"`` ) or as an object
            with an ``algorithm`` field and an optional ``level`` (gzip only, 1–9).
        :type compression: ObservabilityPipelineClickhouseDestinationCompression, optional

        :param database: Optional ClickHouse database name. If omitted, the user's default database on the ClickHouse server is used.
        :type database: str, optional

        :param date_time_best_effort: When ``true`` , enables flexible DateTime parsing on the ClickHouse server side.
        :type date_time_best_effort: bool, optional

        :param endpoint_url_key: Name of the environment variable or secret that contains the ClickHouse HTTP endpoint URL.
            Defaults to ``DESTINATION_CLICKHOUSE_ENDPOINT_URL`` (prefixed with ``DD_OP_`` at runtime).
        :type endpoint_url_key: str, optional

        :param format: Insert format for events sent to ClickHouse.

            * ``json_each_row`` : Maps event fields to columns by name (ClickHouse ``JSONEachRow`` ).
            * ``json_as_object`` : Inserts each event into a single ``Object('json')`` / ``JSON`` column (ClickHouse ``JSONAsObject`` ).
            * ``json_as_string`` : Inserts each event into a single ``String`` -typed column as raw JSON (ClickHouse ``JSONAsString`` ).
            * ``arrow_stream`` : Batches events using Apache Arrow IPC streaming format. Requires ``batch_encoding``.
        :type format: ObservabilityPipelineClickhouseDestinationFormat, optional

        :param id: The unique identifier for this component.
        :type id: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param skip_unknown_fields: When ``true`` , fields not present in the target table schema are dropped instead of causing insert errors.
            When unset, the ClickHouse server's own ``input_format_skip_unknown_fields`` setting applies.
        :type skip_unknown_fields: bool, none_type, optional

        :param table: Target ClickHouse table name. Events are inserted into this table.
        :type table: str

        :param tls: Configuration for enabling TLS encryption between the pipeline component and external services.
        :type tls: ObservabilityPipelineTls, optional

        :param type: The destination type. The value must be ``clickhouse``.
        :type type: ObservabilityPipelineClickhouseDestinationType
        """
        if auth is not unset:
            kwargs["auth"] = auth
        if batch is not unset:
            kwargs["batch"] = batch
        if batch_encoding is not unset:
            kwargs["batch_encoding"] = batch_encoding
        if compression is not unset:
            kwargs["compression"] = compression
        if database is not unset:
            kwargs["database"] = database
        if date_time_best_effort is not unset:
            kwargs["date_time_best_effort"] = date_time_best_effort
        if endpoint_url_key is not unset:
            kwargs["endpoint_url_key"] = endpoint_url_key
        if format is not unset:
            kwargs["format"] = format
        if skip_unknown_fields is not unset:
            kwargs["skip_unknown_fields"] = skip_unknown_fields
        if tls is not unset:
            kwargs["tls"] = tls
        super().__init__(kwargs)

        self_.id = id
        self_.inputs = inputs
        self_.table = table
        self_.type = type
