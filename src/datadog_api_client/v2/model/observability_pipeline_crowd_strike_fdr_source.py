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
    from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
    from datadog_api_client.v2.model.observability_pipeline_crowd_strike_fdr_source_type import (
        ObservabilityPipelineCrowdStrikeFdrSourceType,
    )


class ObservabilityPipelineCrowdStrikeFdrSource(ModelNormal):
    validations = {
        "client_concurrency": {
            "inclusive_maximum": 9007199254740991,
            "inclusive_minimum": 1,
        },
        "max_number_of_messages": {
            "inclusive_maximum": 10,
            "inclusive_minimum": 1,
        },
        "visibility_timeout_secs": {
            "inclusive_maximum": 43200,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
        from datadog_api_client.v2.model.observability_pipeline_crowd_strike_fdr_source_type import (
            ObservabilityPipelineCrowdStrikeFdrSourceType,
        )

        return {
            "access_key_id_key": (str,),
            "client_concurrency": (int,),
            "id": (str,),
            "max_number_of_messages": (int,),
            "region": (str,),
            "secret_access_key_key": (str,),
            "tls": (ObservabilityPipelineTls,),
            "type": (ObservabilityPipelineCrowdStrikeFdrSourceType,),
            "url_key": (str,),
            "visibility_timeout_secs": (int,),
        }

    attribute_map = {
        "access_key_id_key": "access_key_id_key",
        "client_concurrency": "client_concurrency",
        "id": "id",
        "max_number_of_messages": "max_number_of_messages",
        "region": "region",
        "secret_access_key_key": "secret_access_key_key",
        "tls": "tls",
        "type": "type",
        "url_key": "url_key",
        "visibility_timeout_secs": "visibility_timeout_secs",
    }

    def __init__(
        self_,
        id: str,
        region: str,
        type: ObservabilityPipelineCrowdStrikeFdrSourceType,
        access_key_id_key: Union[str, UnsetType] = unset,
        client_concurrency: Union[int, UnsetType] = unset,
        max_number_of_messages: Union[int, UnsetType] = unset,
        secret_access_key_key: Union[str, UnsetType] = unset,
        tls: Union[ObservabilityPipelineTls, UnsetType] = unset,
        url_key: Union[str, UnsetType] = unset,
        visibility_timeout_secs: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``crowdstrike_fdr`` source ingests CrowdStrike Falcon Data Replicator (FDR) data.
        It reads file notifications from the CrowdStrike-managed SQS queue for your FDR feed and downloads the referenced objects from the CrowdStrike-managed S3 bucket.

        **Supported pipeline types:** logs

        :param access_key_id_key: Name of the environment variable or secret that holds the AWS access key ID that CrowdStrike generated for the FDR feed.
        :type access_key_id_key: str, optional

        :param client_concurrency: Number of concurrent tasks polling the SQS queue. Defaults to the number of Worker threads.
        :type client_concurrency: int, optional

        :param id: The unique identifier for this component. Used in other parts of the pipeline to reference this component (for example, as the ``input`` to downstream components).
        :type id: str

        :param max_number_of_messages: Maximum number of SQS messages to receive per poll. Each message can reference multiple files. Defaults to 1.
        :type max_number_of_messages: int, optional

        :param region: AWS region of the FDR feed's SQS queue and S3 bucket.
        :type region: str

        :param secret_access_key_key: Name of the environment variable or secret that holds the AWS secret access key that CrowdStrike generated for the FDR feed.
        :type secret_access_key_key: str, optional

        :param tls: Configuration for enabling TLS encryption between the pipeline component and external services.
        :type tls: ObservabilityPipelineTls, optional

        :param type: The source type. Always ``crowdstrike_fdr``.
        :type type: ObservabilityPipelineCrowdStrikeFdrSourceType

        :param url_key: Name of the environment variable or secret that holds the URL of the FDR feed's SQS queue.
        :type url_key: str, optional

        :param visibility_timeout_secs: Number of seconds a received SQS message is hidden from other consumers. Set it higher than the time needed to download and process the largest FDR file. Defaults to 300.
        :type visibility_timeout_secs: int, optional
        """
        if access_key_id_key is not unset:
            kwargs["access_key_id_key"] = access_key_id_key
        if client_concurrency is not unset:
            kwargs["client_concurrency"] = client_concurrency
        if max_number_of_messages is not unset:
            kwargs["max_number_of_messages"] = max_number_of_messages
        if secret_access_key_key is not unset:
            kwargs["secret_access_key_key"] = secret_access_key_key
        if tls is not unset:
            kwargs["tls"] = tls
        if url_key is not unset:
            kwargs["url_key"] = url_key
        if visibility_timeout_secs is not unset:
            kwargs["visibility_timeout_secs"] = visibility_timeout_secs
        super().__init__(kwargs)

        self_.id = id
        self_.region = region
        self_.type = type
