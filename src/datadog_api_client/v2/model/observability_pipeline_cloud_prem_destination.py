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
    from datadog_api_client.v2.model.observability_pipeline_cloud_prem_destination_type import (
        ObservabilityPipelineCloudPremDestinationType,
    )


class ObservabilityPipelineCloudPremDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_cloud_prem_destination_type import (
            ObservabilityPipelineCloudPremDestinationType,
        )

        return {
            "endpoint_url_key": (str,),
            "id": (str,),
            "inputs": ([str],),
            "type": (ObservabilityPipelineCloudPremDestinationType,),
        }

    attribute_map = {
        "endpoint_url_key": "endpoint_url_key",
        "id": "id",
        "inputs": "inputs",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        inputs: List[str],
        type: ObservabilityPipelineCloudPremDestinationType,
        endpoint_url_key: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``cloud_prem`` destination sends logs to Datadog CloudPrem.

        **Supported pipeline types:** logs

        :param endpoint_url_key: Name of the environment variable or secret that holds the CloudPrem endpoint URL.
        :type endpoint_url_key: str, optional

        :param id: The unique identifier for this component.
        :type id: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param type: The destination type. The value should always be ``cloud_prem``.
        :type type: ObservabilityPipelineCloudPremDestinationType
        """
        if endpoint_url_key is not unset:
            kwargs["endpoint_url_key"] = endpoint_url_key
        super().__init__(kwargs)

        self_.id = id
        self_.inputs = inputs
        self_.type = type
