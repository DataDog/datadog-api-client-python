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
    from datadog_api_client.v2.model.observability_pipeline_google_chronicle_destination_encoding import (
        ObservabilityPipelineGoogleChronicleDestinationEncoding,
    )
    from datadog_api_client.v2.model.observability_pipeline_google_chronicle_destination_type import (
        ObservabilityPipelineGoogleChronicleDestinationType,
    )


class ObservabilityPipelineGoogleChronicleDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_gcp_auth import ObservabilityPipelineGcpAuth
        from datadog_api_client.v2.model.observability_pipeline_google_chronicle_destination_encoding import (
            ObservabilityPipelineGoogleChronicleDestinationEncoding,
        )
        from datadog_api_client.v2.model.observability_pipeline_google_chronicle_destination_type import (
            ObservabilityPipelineGoogleChronicleDestinationType,
        )

        return {
            "auth": (ObservabilityPipelineGcpAuth,),
            "customer_id": (str,),
            "encoding": (ObservabilityPipelineGoogleChronicleDestinationEncoding,),
            "id": (str,),
            "inputs": ([str],),
            "log_type": (str,),
            "type": (ObservabilityPipelineGoogleChronicleDestinationType,),
        }

    attribute_map = {
        "auth": "auth",
        "customer_id": "customer_id",
        "encoding": "encoding",
        "id": "id",
        "inputs": "inputs",
        "log_type": "log_type",
        "type": "type",
    }

    def __init__(
        self_,
        auth: ObservabilityPipelineGcpAuth,
        customer_id: str,
        id: str,
        inputs: List[str],
        type: ObservabilityPipelineGoogleChronicleDestinationType,
        encoding: Union[ObservabilityPipelineGoogleChronicleDestinationEncoding, UnsetType] = unset,
        log_type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``google_chronicle`` destination sends logs to Google Chronicle.

        :param auth: GCP credentials used to authenticate with Google Cloud Storage.
        :type auth: ObservabilityPipelineGcpAuth

        :param customer_id: The Google Chronicle customer ID.
        :type customer_id: str

        :param encoding: The encoding format for the logs sent to Chronicle.
        :type encoding: ObservabilityPipelineGoogleChronicleDestinationEncoding, optional

        :param id: The unique identifier for this component.
        :type id: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param log_type: The log type metadata associated with the Chronicle destination.
        :type log_type: str, optional

        :param type: The destination type. The value should always be ``google_chronicle``.
        :type type: ObservabilityPipelineGoogleChronicleDestinationType
        """
        if encoding is not unset:
            kwargs["encoding"] = encoding
        if log_type is not unset:
            kwargs["log_type"] = log_type
        super().__init__(kwargs)

        self_.auth = auth
        self_.customer_id = customer_id
        self_.id = id
        self_.inputs = inputs
        self_.type = type
