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
    from datadog_api_client.v2.model.security_findings_data import SecurityFindingsData
    from datadog_api_client.v2.model.security_findings_links import SecurityFindingsLinks
    from datadog_api_client.v2.model.security_findings_meta import SecurityFindingsMeta


class ListSecurityFindingsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_findings_data import SecurityFindingsData
        from datadog_api_client.v2.model.security_findings_links import SecurityFindingsLinks
        from datadog_api_client.v2.model.security_findings_meta import SecurityFindingsMeta

        return {
            "data": ([SecurityFindingsData],),
            "links": (SecurityFindingsLinks,),
            "meta": (SecurityFindingsMeta,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[SecurityFindingsData], UnsetType] = unset,
        links: Union[SecurityFindingsLinks, UnsetType] = unset,
        meta: Union[SecurityFindingsMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        The expected response schema when listing security findings.

        :param data: Array of security findings matching the search query.
        :type data: [SecurityFindingsData], optional

        :param links: Links for pagination.
        :type links: SecurityFindingsLinks, optional

        :param meta: Metadata about the response.
        :type meta: SecurityFindingsMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if links is not unset:
            kwargs["links"] = links
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
