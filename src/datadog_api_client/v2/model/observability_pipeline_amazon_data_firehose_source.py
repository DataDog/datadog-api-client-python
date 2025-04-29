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
    from datadog_api_client.v2.model.observability_pipeline_aws_auth import ObservabilityPipelineAwsAuth
    from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
    from datadog_api_client.v2.model.observability_pipeline_amazon_data_firehose_source_type import (
        ObservabilityPipelineAmazonDataFirehoseSourceType,
    )


class ObservabilityPipelineAmazonDataFirehoseSource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_aws_auth import ObservabilityPipelineAwsAuth
        from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
        from datadog_api_client.v2.model.observability_pipeline_amazon_data_firehose_source_type import (
            ObservabilityPipelineAmazonDataFirehoseSourceType,
        )

        return {
            "auth": (ObservabilityPipelineAwsAuth,),
            "id": (str,),
            "tls": (ObservabilityPipelineTls,),
            "type": (ObservabilityPipelineAmazonDataFirehoseSourceType,),
        }

    attribute_map = {
        "auth": "auth",
        "id": "id",
        "tls": "tls",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: ObservabilityPipelineAmazonDataFirehoseSourceType,
        auth: Union[ObservabilityPipelineAwsAuth, UnsetType] = unset,
        tls: Union[ObservabilityPipelineTls, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``amazon_data_firehose`` source ingests logs from AWS Data Firehose.

        :param auth: AWS authentication credentials used for accessing AWS services such as S3.
            If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).
        :type auth: ObservabilityPipelineAwsAuth, optional

        :param id: The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
        :type id: str

        :param tls: Configuration for enabling TLS encryption between the pipeline component and external services.
        :type tls: ObservabilityPipelineTls, optional

        :param type: The source type. The value should always be ``amazon_data_firehose``.
        :type type: ObservabilityPipelineAmazonDataFirehoseSourceType
        """
        if auth is not unset:
            kwargs["auth"] = auth
        if tls is not unset:
            kwargs["tls"] = tls
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
