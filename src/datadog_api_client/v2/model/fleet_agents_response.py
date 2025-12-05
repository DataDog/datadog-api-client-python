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
    from datadog_api_client.v2.model.fleet_agents_response_data import FleetAgentsResponseData
    from datadog_api_client.v2.model.fleet_agents_response_meta import FleetAgentsResponseMeta


class FleetAgentsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_agents_response_data import FleetAgentsResponseData
        from datadog_api_client.v2.model.fleet_agents_response_meta import FleetAgentsResponseMeta

        return {
            "data": (FleetAgentsResponseData,),
            "meta": (FleetAgentsResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_, data: FleetAgentsResponseData, meta: Union[FleetAgentsResponseMeta, UnsetType] = unset, **kwargs
    ):
        """
        Response containing a paginated list of Datadog Agents.

        :param data: The response data containing status and agents array.
        :type data: FleetAgentsResponseData

        :param meta: Metadata for the list of agents response.
        :type meta: FleetAgentsResponseMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
