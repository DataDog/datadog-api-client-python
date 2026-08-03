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
    from datadog_api_client.v2.model.fleet_agent_versions_v2_page import FleetAgentVersionsV2Page


class FleetAgentVersionsV2ResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_agent_versions_v2_page import FleetAgentVersionsV2Page

        return {
            "page": (FleetAgentVersionsV2Page,),
        }

    attribute_map = {
        "page": "page",
    }

    def __init__(self_, page: Union[FleetAgentVersionsV2Page, UnsetType] = unset, **kwargs):
        """
        Metadata for the v2 list of agent versions.

        :param page: Pagination details for the v2 list of agent versions.
        :type page: FleetAgentVersionsV2Page, optional
        """
        if page is not unset:
            kwargs["page"] = page
        super().__init__(kwargs)
