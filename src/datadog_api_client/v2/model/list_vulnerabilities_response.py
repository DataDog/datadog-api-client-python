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
    from datadog_api_client.v2.model.vulnerability import Vulnerability
    from datadog_api_client.v2.model.links import Links
    from datadog_api_client.v2.model.metadata import Metadata


class ListVulnerabilitiesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.vulnerability import Vulnerability
        from datadog_api_client.v2.model.links import Links
        from datadog_api_client.v2.model.metadata import Metadata

        return {
            "data": ([Vulnerability],),
            "links": (Links,),
            "meta": (Metadata,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
        "meta": "meta",
    }

    def __init__(self_, data: List[Vulnerability], links: Links, meta: Metadata, **kwargs):
        """
        The expected response schema when listing vulnerabilities.

        :param data: List of vulnerabilities.
        :type data: [Vulnerability]

        :param links: The JSON:API links related to pagination.
        :type links: Links

        :param meta: The metadata related to this request.
        :type meta: Metadata
        """
        super().__init__(kwargs)

        self_.data = data
        self_.links = links
        self_.meta = meta
