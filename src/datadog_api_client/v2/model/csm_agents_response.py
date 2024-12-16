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
    from datadog_api_client.v2.model.csm_agent_data import CsmAgentData
    from datadog_api_client.v2.model.csm_agents_metadata import CSMAgentsMetadata


class CsmAgentsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.csm_agent_data import CsmAgentData
        from datadog_api_client.v2.model.csm_agents_metadata import CSMAgentsMetadata

        return {
            "data": ([CsmAgentData],),
            "meta": (CSMAgentsMetadata,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[CsmAgentData], UnsetType] = unset,
        meta: Union[CSMAgentsMetadata, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response object that includes a list of CSM Agents.

        :param data: A list of Agents.
        :type data: [CsmAgentData], optional

        :param meta: Metadata related to the paginated response.
        :type meta: CSMAgentsMetadata, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
