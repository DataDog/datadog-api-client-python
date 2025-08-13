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
    from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
    from datadog_api_client.v2.model.observability_pipeline_amazon_security_lake_destination_type import (
        ObservabilityPipelineAmazonSecurityLakeDestinationType,
    )


class ObservabilityPipelineAmazonSecurityLakeDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_aws_auth import ObservabilityPipelineAwsAuth
        from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
        from datadog_api_client.v2.model.observability_pipeline_amazon_security_lake_destination_type import (
            ObservabilityPipelineAmazonSecurityLakeDestinationType,
        )

        return {
            "auth": (ObservabilityPipelineAwsAuth,),
            "bucket": (str,),
            "custom_source_name": (str,),
            "id": (str,),
            "inputs": ([str],),
            "region": (str,),
            "tls": (ObservabilityPipelineTls,),
            "type": (ObservabilityPipelineAmazonSecurityLakeDestinationType,),
        }

    attribute_map = {
        "auth": "auth",
        "bucket": "bucket",
        "custom_source_name": "custom_source_name",
        "id": "id",
        "inputs": "inputs",
        "region": "region",
        "tls": "tls",
        "type": "type",
    }

    def __init__(
        self_,
        bucket: str,
        custom_source_name: str,
        id: str,
        inputs: List[str],
        region: str,
        type: ObservabilityPipelineAmazonSecurityLakeDestinationType,
        auth: Union[ObservabilityPipelineAwsAuth, UnsetType] = unset,
        tls: Union[ObservabilityPipelineTls, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``amazon_security_lake`` destination sends your logs to Amazon Security Lake.

        :param auth: AWS authentication credentials used for accessing AWS services such as S3.
            If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
        :type auth: ObservabilityPipelineAwsAuth, optional

        :param bucket: Name of the Amazon S3 bucket in Security Lake (3-63 characters).
        :type bucket: str

        :param custom_source_name: Custom source name for the logs in Security Lake.
        :type custom_source_name: str

        :param id: Unique identifier for the destination component.
        :type id: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param region: AWS region of the S3 bucket.
        :type region: str

        :param tls: Configuration for enabling TLS encryption between the pipeline component and external services.
        :type tls: ObservabilityPipelineTls, optional

        :param type: The destination type. Always ``amazon_security_lake``.
        :type type: ObservabilityPipelineAmazonSecurityLakeDestinationType
        """
        if auth is not unset:
            kwargs["auth"] = auth
        if tls is not unset:
            kwargs["tls"] = tls
        super().__init__(kwargs)

        self_.bucket = bucket
        self_.custom_source_name = custom_source_name
        self_.id = id
        self_.inputs = inputs
        self_.region = region
        self_.type = type
