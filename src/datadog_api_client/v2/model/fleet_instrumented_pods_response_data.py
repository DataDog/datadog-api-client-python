# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.fleet_instrumented_pods_response_data_attributes import (
        FleetInstrumentedPodsResponseDataAttributes,
    )


class FleetInstrumentedPodsResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_instrumented_pods_response_data_attributes import (
            FleetInstrumentedPodsResponseDataAttributes,
        )

        return {
            "attributes": (FleetInstrumentedPodsResponseDataAttributes,),
            "id": (str,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: FleetInstrumentedPodsResponseDataAttributes, id: str, type: str, **kwargs):
        """
        The response data containing the cluster name and instrumented pod groups.

        :param attributes: Attributes of the instrumented pods response containing the list of pod groups.
        :type attributes: FleetInstrumentedPodsResponseDataAttributes

        :param id: The cluster name identifier.
        :type id: str

        :param type: Resource type.
        :type type: str
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
