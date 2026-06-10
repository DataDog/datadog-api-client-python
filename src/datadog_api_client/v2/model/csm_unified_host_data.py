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
    from datadog_api_client.v2.model.csm_unified_host_attributes import CsmUnifiedHostAttributes
    from datadog_api_client.v2.model.csm_unified_host_type import CsmUnifiedHostType


class CsmUnifiedHostData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.csm_unified_host_attributes import CsmUnifiedHostAttributes
        from datadog_api_client.v2.model.csm_unified_host_type import CsmUnifiedHostType

        return {
            "attributes": (CsmUnifiedHostAttributes,),
            "id": (str,),
            "type": (CsmUnifiedHostType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: CsmUnifiedHostAttributes, id: str, type: CsmUnifiedHostType, **kwargs):
        """
        A single unified host resource, combining agent and agentless data.

        :param attributes: Attributes of a unified host, combining data from agent and agentless sources.
        :type attributes: CsmUnifiedHostAttributes

        :param id: The resource identifier of the unified host.
        :type id: str

        :param type: The JSON:API type for unified host resources. The value should always be ``unified_host``.
        :type type: CsmUnifiedHostType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
