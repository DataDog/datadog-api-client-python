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
    from datadog_api_client.v2.model.tag_indexing_rule_exemption_data import TagIndexingRuleExemptionData
    from datadog_api_client.v2.model.metrics_list_response_links import MetricsListResponseLinks
    from datadog_api_client.v2.model.metric_pagination_meta import MetricPaginationMeta


class TagIndexingRuleExemptionsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_indexing_rule_exemption_data import TagIndexingRuleExemptionData
        from datadog_api_client.v2.model.metrics_list_response_links import MetricsListResponseLinks
        from datadog_api_client.v2.model.metric_pagination_meta import MetricPaginationMeta

        return {
            "data": ([TagIndexingRuleExemptionData],),
            "links": (MetricsListResponseLinks,),
            "meta": (MetricPaginationMeta,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[TagIndexingRuleExemptionData], UnsetType] = unset,
        links: Union[MetricsListResponseLinks, UnsetType] = unset,
        meta: Union[MetricPaginationMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing a page of tag indexing rule exemptions.

        :param data: Array of tag indexing rule exemption objects.
        :type data: [TagIndexingRuleExemptionData], optional

        :param links: Pagination links. Only present if pagination query parameters were provided.
        :type links: MetricsListResponseLinks, optional

        :param meta: Response metadata object.
        :type meta: MetricPaginationMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if links is not unset:
            kwargs["links"] = links
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
