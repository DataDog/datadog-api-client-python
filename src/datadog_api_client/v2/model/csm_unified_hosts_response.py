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
    from datadog_api_client.v2.model.csm_unified_host_data import CsmUnifiedHostData
    from datadog_api_client.v2.model.csm_unified_hosts_meta import CsmUnifiedHostsMeta


class CsmUnifiedHostsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.csm_unified_host_data import CsmUnifiedHostData
        from datadog_api_client.v2.model.csm_unified_hosts_meta import CsmUnifiedHostsMeta

        return {
            "data": ([CsmUnifiedHostData],),
            "meta": (CsmUnifiedHostsMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self_, data: List[CsmUnifiedHostData], meta: CsmUnifiedHostsMeta, **kwargs):
        """
        The response returned when listing unified hosts.

        :param data: The list of unified hosts for the current page.
        :type data: [CsmUnifiedHostData]

        :param meta: Pagination metadata for a unified hosts list response.
        :type meta: CsmUnifiedHostsMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
