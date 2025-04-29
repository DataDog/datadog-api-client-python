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
    from datadog_api_client.v2.model.observability_pipeline_gcp_auth import ObservabilityPipelineGcpAuth
    from datadog_api_client.v2.model.observability_pipeline_decoding import ObservabilityPipelineDecoding
    from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
    from datadog_api_client.v2.model.observability_pipeline_google_pub_sub_source_type import (
        ObservabilityPipelineGooglePubSubSourceType,
    )


class ObservabilityPipelineGooglePubSubSource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_gcp_auth import ObservabilityPipelineGcpAuth
        from datadog_api_client.v2.model.observability_pipeline_decoding import ObservabilityPipelineDecoding
        from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
        from datadog_api_client.v2.model.observability_pipeline_google_pub_sub_source_type import (
            ObservabilityPipelineGooglePubSubSourceType,
        )

        return {
            "auth": (ObservabilityPipelineGcpAuth,),
            "decoding": (ObservabilityPipelineDecoding,),
            "id": (str,),
            "project": (str,),
            "subscription": (str,),
            "tls": (ObservabilityPipelineTls,),
            "type": (ObservabilityPipelineGooglePubSubSourceType,),
        }

    attribute_map = {
        "auth": "auth",
        "decoding": "decoding",
        "id": "id",
        "project": "project",
        "subscription": "subscription",
        "tls": "tls",
        "type": "type",
    }

    def __init__(
        self_,
        auth: ObservabilityPipelineGcpAuth,
        decoding: ObservabilityPipelineDecoding,
        id: str,
        project: str,
        subscription: str,
        type: ObservabilityPipelineGooglePubSubSourceType,
        tls: Union[ObservabilityPipelineTls, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``google_pubsub`` source ingests logs from a Google Cloud Pub/Sub subscription.

        :param auth: GCP credentials used to authenticate with Google Cloud Storage.
        :type auth: ObservabilityPipelineGcpAuth

        :param decoding: The decoding format used to interpret incoming logs.
        :type decoding: ObservabilityPipelineDecoding

        :param id: The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
        :type id: str

        :param project: The GCP project ID that owns the Pub/Sub subscription.
        :type project: str

        :param subscription: The Pub/Sub subscription name from which messages are consumed.
        :type subscription: str

        :param tls: Configuration for enabling TLS encryption between the pipeline component and external services.
        :type tls: ObservabilityPipelineTls, optional

        :param type: The source type. The value should always be ``google_pubsub``.
        :type type: ObservabilityPipelineGooglePubSubSourceType
        """
        if tls is not unset:
            kwargs["tls"] = tls
        super().__init__(kwargs)

        self_.auth = auth
        self_.decoding = decoding
        self_.id = id
        self_.project = project
        self_.subscription = subscription
        self_.type = type
