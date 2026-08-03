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
    from datadog_api_client.v2.model.fleet_agents_v2_page import FleetAgentsV2Page


class FleetAgentsV2ResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_agents_v2_page import FleetAgentsV2Page

        return {
            "page": (FleetAgentsV2Page,),
        }

    attribute_map = {
        "page": "page",
    }

    def __init__(self_, page: Union[FleetAgentsV2Page, UnsetType] = unset, **kwargs):
        """
        Metadata for the v2 list of agents, including pagination information.

        :param page: Pagination details for the v2 list of agents.
        :type page: FleetAgentsV2Page, optional
        """
        if page is not unset:
            kwargs["page"] = page
        super().__init__(kwargs)
