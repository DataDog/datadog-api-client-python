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
    from datadog_api_client.v2.model.csm_agentless_host_facet_attributes import CsmAgentlessHostFacetAttributes
    from datadog_api_client.v2.model.csm_unified_host_facet_type import CsmUnifiedHostFacetType


class CsmUnifiedHostFacetData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.csm_agentless_host_facet_attributes import CsmAgentlessHostFacetAttributes
        from datadog_api_client.v2.model.csm_unified_host_facet_type import CsmUnifiedHostFacetType

        return {
            "attributes": (CsmAgentlessHostFacetAttributes,),
            "id": (str,),
            "type": (CsmUnifiedHostFacetType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: CsmAgentlessHostFacetAttributes, id: str, type: CsmUnifiedHostFacetType, **kwargs):
        """
        A single unified host facet resource.

        :param attributes: Attributes of an agentless host facet.
        :type attributes: CsmAgentlessHostFacetAttributes

        :param id: The identifier of the facet, corresponding to the field path.
        :type id: str

        :param type: The JSON:API type for unified host facet resources. The value should always be ``unified_host_facet``.
        :type type: CsmUnifiedHostFacetType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
