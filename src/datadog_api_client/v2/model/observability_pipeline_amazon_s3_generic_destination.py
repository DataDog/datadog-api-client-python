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
    from datadog_api_client.v2.model.observability_pipeline_aws_auth import ObservabilityPipelineAwsAuth
    from datadog_api_client.v2.model.observability_pipeline_amazon_s3_generic_batch_settings import (
        ObservabilityPipelineAmazonS3GenericBatchSettings,
    )
    from datadog_api_client.v2.model.observability_pipeline_amazon_s3_generic_compression import (
        ObservabilityPipelineAmazonS3GenericCompression,
    )
    from datadog_api_client.v2.model.observability_pipeline_amazon_s3_generic_encoding import (
        ObservabilityPipelineAmazonS3GenericEncoding,
    )
    from datadog_api_client.v2.model.observability_pipeline_amazon_s3_destination_storage_class import (
        ObservabilityPipelineAmazonS3DestinationStorageClass,
    )
    from datadog_api_client.v2.model.observability_pipeline_amazon_s3_generic_destination_type import (
        ObservabilityPipelineAmazonS3GenericDestinationType,
    )
    from datadog_api_client.v2.model.observability_pipeline_amazon_s3_generic_compression_zstd import (
        ObservabilityPipelineAmazonS3GenericCompressionZstd,
    )
    from datadog_api_client.v2.model.observability_pipeline_amazon_s3_generic_compression_gzip import (
        ObservabilityPipelineAmazonS3GenericCompressionGzip,
    )
    from datadog_api_client.v2.model.observability_pipeline_amazon_s3_generic_compression_snappy import (
        ObservabilityPipelineAmazonS3GenericCompressionSnappy,
    )
    from datadog_api_client.v2.model.observability_pipeline_amazon_s3_generic_encoding_json import (
        ObservabilityPipelineAmazonS3GenericEncodingJson,
    )
    from datadog_api_client.v2.model.observability_pipeline_amazon_s3_generic_encoding_parquet import (
        ObservabilityPipelineAmazonS3GenericEncodingParquet,
    )


class ObservabilityPipelineAmazonS3GenericDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_aws_auth import ObservabilityPipelineAwsAuth
        from datadog_api_client.v2.model.observability_pipeline_amazon_s3_generic_batch_settings import (
            ObservabilityPipelineAmazonS3GenericBatchSettings,
        )
        from datadog_api_client.v2.model.observability_pipeline_amazon_s3_generic_compression import (
            ObservabilityPipelineAmazonS3GenericCompression,
        )
        from datadog_api_client.v2.model.observability_pipeline_amazon_s3_generic_encoding import (
            ObservabilityPipelineAmazonS3GenericEncoding,
        )
        from datadog_api_client.v2.model.observability_pipeline_amazon_s3_destination_storage_class import (
            ObservabilityPipelineAmazonS3DestinationStorageClass,
        )
        from datadog_api_client.v2.model.observability_pipeline_amazon_s3_generic_destination_type import (
            ObservabilityPipelineAmazonS3GenericDestinationType,
        )

        return {
            "auth": (ObservabilityPipelineAwsAuth,),
            "batch_settings": (ObservabilityPipelineAmazonS3GenericBatchSettings,),
            "bucket": (str,),
            "compression": (ObservabilityPipelineAmazonS3GenericCompression,),
            "encoding": (ObservabilityPipelineAmazonS3GenericEncoding,),
            "id": (str,),
            "inputs": ([str],),
            "key_prefix": (str,),
            "region": (str,),
            "storage_class": (ObservabilityPipelineAmazonS3DestinationStorageClass,),
            "type": (ObservabilityPipelineAmazonS3GenericDestinationType,),
        }

    attribute_map = {
        "auth": "auth",
        "batch_settings": "batch_settings",
        "bucket": "bucket",
        "compression": "compression",
        "encoding": "encoding",
        "id": "id",
        "inputs": "inputs",
        "key_prefix": "key_prefix",
        "region": "region",
        "storage_class": "storage_class",
        "type": "type",
    }

    def __init__(
        self_,
        bucket: str,
        compression: Union[
            ObservabilityPipelineAmazonS3GenericCompression,
            ObservabilityPipelineAmazonS3GenericCompressionZstd,
            ObservabilityPipelineAmazonS3GenericCompressionGzip,
            ObservabilityPipelineAmazonS3GenericCompressionSnappy,
        ],
        encoding: Union[
            ObservabilityPipelineAmazonS3GenericEncoding,
            ObservabilityPipelineAmazonS3GenericEncodingJson,
            ObservabilityPipelineAmazonS3GenericEncodingParquet,
        ],
        id: str,
        inputs: List[str],
        region: str,
        storage_class: ObservabilityPipelineAmazonS3DestinationStorageClass,
        type: ObservabilityPipelineAmazonS3GenericDestinationType,
        auth: Union[ObservabilityPipelineAwsAuth, UnsetType] = unset,
        batch_settings: Union[ObservabilityPipelineAmazonS3GenericBatchSettings, UnsetType] = unset,
        key_prefix: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``amazon_s3_generic`` destination sends your logs to an Amazon S3 bucket.

        **Supported pipeline types:** logs

        :param auth: AWS authentication credentials used for accessing AWS services such as S3.
            If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
        :type auth: ObservabilityPipelineAwsAuth, optional

        :param batch_settings: Event batching settings
        :type batch_settings: ObservabilityPipelineAmazonS3GenericBatchSettings, optional

        :param bucket: S3 bucket name.
        :type bucket: str

        :param compression: Compression algorithm applied to encoded logs.
        :type compression: ObservabilityPipelineAmazonS3GenericCompression

        :param encoding: Encoding format for the destination.
        :type encoding: ObservabilityPipelineAmazonS3GenericEncoding

        :param id: Unique identifier for the destination component.
        :type id: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param key_prefix: Optional prefix for object keys.
        :type key_prefix: str, optional

        :param region: AWS region of the S3 bucket.
        :type region: str

        :param storage_class: S3 storage class.
        :type storage_class: ObservabilityPipelineAmazonS3DestinationStorageClass

        :param type: The destination type. Always ``amazon_s3_generic``.
        :type type: ObservabilityPipelineAmazonS3GenericDestinationType
        """
        if auth is not unset:
            kwargs["auth"] = auth
        if batch_settings is not unset:
            kwargs["batch_settings"] = batch_settings
        if key_prefix is not unset:
            kwargs["key_prefix"] = key_prefix
        super().__init__(kwargs)

        self_.bucket = bucket
        self_.compression = compression
        self_.encoding = encoding
        self_.id = id
        self_.inputs = inputs
        self_.region = region
        self_.storage_class = storage_class
        self_.type = type
