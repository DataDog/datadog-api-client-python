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
    from datadog_api_client.v2.model.csm_agentless_host_attributes import CsmAgentlessHostAttributes
    from datadog_api_client.v2.model.csm_agentless_host_type import CsmAgentlessHostType


class CsmAgentlessHostData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.csm_agentless_host_attributes import CsmAgentlessHostAttributes
        from datadog_api_client.v2.model.csm_agentless_host_type import CsmAgentlessHostType

        return {
            "attributes": (CsmAgentlessHostAttributes,),
            "id": (str,),
            "type": (CsmAgentlessHostType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: CsmAgentlessHostAttributes, id: str, type: CsmAgentlessHostType, **kwargs):
        """
        A single agentless host resource.

        :param attributes: Attributes of an agentless host.
        :type attributes: CsmAgentlessHostAttributes

        :param id: The resource identifier of the agentless host.
        :type id: str

        :param type: The JSON:API type for agentless host resources. The value should always be ``agentless_host``.
        :type type: CsmAgentlessHostType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
