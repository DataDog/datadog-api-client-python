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
    from datadog_api_client.v2.model.observability_pipeline_amazon_s3_destination_storage_class import (
        ObservabilityPipelineAmazonS3DestinationStorageClass,
    )
    from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
    from datadog_api_client.v2.model.observability_pipeline_amazon_s3_destination_type import (
        ObservabilityPipelineAmazonS3DestinationType,
    )


class ObservabilityPipelineAmazonS3Destination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_aws_auth import ObservabilityPipelineAwsAuth
        from datadog_api_client.v2.model.observability_pipeline_amazon_s3_destination_storage_class import (
            ObservabilityPipelineAmazonS3DestinationStorageClass,
        )
        from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
        from datadog_api_client.v2.model.observability_pipeline_amazon_s3_destination_type import (
            ObservabilityPipelineAmazonS3DestinationType,
        )

        return {
            "auth": (ObservabilityPipelineAwsAuth,),
            "bucket": (str,),
            "id": (str,),
            "inputs": ([str],),
            "key_prefix": (str,),
            "region": (str,),
            "storage_class": (ObservabilityPipelineAmazonS3DestinationStorageClass,),
            "tls": (ObservabilityPipelineTls,),
            "type": (ObservabilityPipelineAmazonS3DestinationType,),
        }

    attribute_map = {
        "auth": "auth",
        "bucket": "bucket",
        "id": "id",
        "inputs": "inputs",
        "key_prefix": "key_prefix",
        "region": "region",
        "storage_class": "storage_class",
        "tls": "tls",
        "type": "type",
    }

    def __init__(
        self_,
        bucket: str,
        id: str,
        inputs: List[str],
        region: str,
        storage_class: ObservabilityPipelineAmazonS3DestinationStorageClass,
        type: ObservabilityPipelineAmazonS3DestinationType,
        auth: Union[ObservabilityPipelineAwsAuth, UnsetType] = unset,
        key_prefix: Union[str, UnsetType] = unset,
        tls: Union[ObservabilityPipelineTls, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``amazon_s3`` destination sends your logs in Datadog-rehydratable format to an Amazon S3 bucket for archiving.

        :param auth: AWS authentication credentials used for accessing AWS services such as S3.
            If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
        :type auth: ObservabilityPipelineAwsAuth, optional

        :param bucket: S3 bucket name.
        :type bucket: str

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

        :param tls: Configuration for enabling TLS encryption between the pipeline component and external services.
        :type tls: ObservabilityPipelineTls, optional

        :param type: The destination type. Always ``amazon_s3``.
        :type type: ObservabilityPipelineAmazonS3DestinationType
        """
        if auth is not unset:
            kwargs["auth"] = auth
        if key_prefix is not unset:
            kwargs["key_prefix"] = key_prefix
        if tls is not unset:
            kwargs["tls"] = tls
        super().__init__(kwargs)

        self_.bucket = bucket
        self_.id = id
        self_.inputs = inputs
        self_.region = region
        self_.storage_class = storage_class
        self_.type = type
