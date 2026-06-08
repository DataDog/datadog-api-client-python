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
    from datadog_api_client.v2.model.tag_indexing_rule_data import TagIndexingRuleData
    from datadog_api_client.v2.model.metrics_list_response_links import MetricsListResponseLinks
    from datadog_api_client.v2.model.tag_indexing_rules_response_meta import TagIndexingRulesResponseMeta


class TagIndexingRulesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_indexing_rule_data import TagIndexingRuleData
        from datadog_api_client.v2.model.metrics_list_response_links import MetricsListResponseLinks
        from datadog_api_client.v2.model.tag_indexing_rules_response_meta import TagIndexingRulesResponseMeta

        return {
            "data": ([TagIndexingRuleData],),
            "links": (MetricsListResponseLinks,),
            "meta": (TagIndexingRulesResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[TagIndexingRuleData], UnsetType] = unset,
        links: Union[MetricsListResponseLinks, UnsetType] = unset,
        meta: Union[TagIndexingRulesResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing a page of tag indexing rules.

        :param data: Array of tag indexing rule objects.
        :type data: [TagIndexingRuleData], optional

        :param links: Pagination links. Only present if pagination query parameters were provided.
        :type links: MetricsListResponseLinks, optional

        :param meta: Pagination metadata for a list of tag indexing rules.
        :type meta: TagIndexingRulesResponseMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if links is not unset:
            kwargs["links"] = links
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
