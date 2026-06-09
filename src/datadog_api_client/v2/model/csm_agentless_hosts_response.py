# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.csm_agentless_host_data import CsmAgentlessHostData
    from datadog_api_client.v2.model.csm_settings_meta import CsmSettingsMeta


class CsmAgentlessHostsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.csm_agentless_host_data import CsmAgentlessHostData
        from datadog_api_client.v2.model.csm_settings_meta import CsmSettingsMeta

        return {
            "data": ([CsmAgentlessHostData],),
            "meta": (CsmSettingsMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self_, data: List[CsmAgentlessHostData], meta: CsmSettingsMeta, **kwargs):
        """
        The response returned when listing agentless hosts.

        :param data: The list of agentless hosts for the current page.
        :type data: [CsmAgentlessHostData]

        :param meta: Pagination metadata for a CSM settings list response.
        :type meta: CsmSettingsMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
