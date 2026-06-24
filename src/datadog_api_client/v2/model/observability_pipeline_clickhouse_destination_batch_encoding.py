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
    from datadog_api_client.v2.model.observability_pipeline_clickhouse_destination_batch_encoding_codec import (
        ObservabilityPipelineClickhouseDestinationBatchEncodingCodec,
    )


class ObservabilityPipelineClickhouseDestinationBatchEncoding(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_clickhouse_destination_batch_encoding_codec import (
            ObservabilityPipelineClickhouseDestinationBatchEncodingCodec,
        )

        return {
            "allow_nullable_fields": (bool,),
            "codec": (ObservabilityPipelineClickhouseDestinationBatchEncodingCodec,),
        }

    attribute_map = {
        "allow_nullable_fields": "allow_nullable_fields",
        "codec": "codec",
    }

    def __init__(
        self_,
        codec: ObservabilityPipelineClickhouseDestinationBatchEncodingCodec,
        allow_nullable_fields: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Batch encoding configuration for the ClickHouse destination.
        Required when ``format`` is ``arrow_stream``. The ``codec`` field must be set to ``arrow_stream``.

        :param allow_nullable_fields: When ``true`` , null values are allowed for non-nullable fields in the ClickHouse schema.
            When ``false`` (default), missing values for non-nullable columns cause encoding errors.
        :type allow_nullable_fields: bool, optional

        :param codec: The codec used for batch encoding. Only ``arrow_stream`` is supported.
        :type codec: ObservabilityPipelineClickhouseDestinationBatchEncodingCodec
        """
        if allow_nullable_fields is not unset:
            kwargs["allow_nullable_fields"] = allow_nullable_fields
        super().__init__(kwargs)

        self_.codec = codec
