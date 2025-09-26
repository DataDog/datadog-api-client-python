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
    from datadog_api_client.v2.model.observability_pipeline_gcp_auth import ObservabilityPipelineGcpAuth
    from datadog_api_client.v2.model.observability_pipeline_google_pub_sub_destination_encoding import (
        ObservabilityPipelineGooglePubSubDestinationEncoding,
    )
    from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
    from datadog_api_client.v2.model.observability_pipeline_google_pub_sub_destination_type import (
        ObservabilityPipelineGooglePubSubDestinationType,
    )


class ObservabilityPipelineGooglePubSubDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_gcp_auth import ObservabilityPipelineGcpAuth
        from datadog_api_client.v2.model.observability_pipeline_google_pub_sub_destination_encoding import (
            ObservabilityPipelineGooglePubSubDestinationEncoding,
        )
        from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
        from datadog_api_client.v2.model.observability_pipeline_google_pub_sub_destination_type import (
            ObservabilityPipelineGooglePubSubDestinationType,
        )

        return {
            "auth": (ObservabilityPipelineGcpAuth,),
            "encoding": (ObservabilityPipelineGooglePubSubDestinationEncoding,),
            "id": (str,),
            "inputs": ([str],),
            "project": (str,),
            "tls": (ObservabilityPipelineTls,),
            "topic": (str,),
            "type": (ObservabilityPipelineGooglePubSubDestinationType,),
        }

    attribute_map = {
        "auth": "auth",
        "encoding": "encoding",
        "id": "id",
        "inputs": "inputs",
        "project": "project",
        "tls": "tls",
        "topic": "topic",
        "type": "type",
    }

    def __init__(
        self_,
        encoding: ObservabilityPipelineGooglePubSubDestinationEncoding,
        id: str,
        inputs: List[str],
        project: str,
        topic: str,
        type: ObservabilityPipelineGooglePubSubDestinationType,
        auth: Union[ObservabilityPipelineGcpAuth, UnsetType] = unset,
        tls: Union[ObservabilityPipelineTls, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``google_pubsub`` destination publishes logs to a Google Cloud Pub/Sub topic.

        :param auth: GCP credentials used to authenticate with Google Cloud Storage.
        :type auth: ObservabilityPipelineGcpAuth, optional

        :param encoding: Encoding format for log events.
        :type encoding: ObservabilityPipelineGooglePubSubDestinationEncoding

        :param id: The unique identifier for this component.
        :type id: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param project: The GCP project ID that owns the Pub/Sub topic.
        :type project: str

        :param tls: Configuration for enabling TLS encryption between the pipeline component and external services.
        :type tls: ObservabilityPipelineTls, optional

        :param topic: The Pub/Sub topic name to publish logs to.
        :type topic: str

        :param type: The destination type. The value should always be ``google_pubsub``.
        :type type: ObservabilityPipelineGooglePubSubDestinationType
        """
        if auth is not unset:
            kwargs["auth"] = auth
        if tls is not unset:
            kwargs["tls"] = tls
        super().__init__(kwargs)

        self_.encoding = encoding
        self_.id = id
        self_.inputs = inputs
        self_.project = project
        self_.topic = topic
        self_.type = type
