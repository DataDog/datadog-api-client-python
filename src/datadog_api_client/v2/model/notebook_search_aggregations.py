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
    from datadog_api_client.v2.model.notebook_search_aggregation_bucket_multi_key import (
        NotebookSearchAggregationBucketMultiKey,
    )
    from datadog_api_client.v2.model.notebook_search_aggregation_bucket_key import NotebookSearchAggregationBucketKey


class NotebookSearchAggregations(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.notebook_search_aggregation_bucket_multi_key import (
            NotebookSearchAggregationBucketMultiKey,
        )
        from datadog_api_client.v2.model.notebook_search_aggregation_bucket_key import (
            NotebookSearchAggregationBucketKey,
        )

        return {
            "author": ([NotebookSearchAggregationBucketMultiKey],),
            "tags": ([NotebookSearchAggregationBucketKey],),
            "template_variables_name": ([NotebookSearchAggregationBucketKey],),
            "type": ([NotebookSearchAggregationBucketKey],),
        }

    attribute_map = {
        "author": "author",
        "tags": "tags",
        "template_variables_name": "template_variables.name",
        "type": "type",
    }

    def __init__(
        self_,
        author: Union[List[NotebookSearchAggregationBucketMultiKey], UnsetType] = unset,
        tags: Union[List[NotebookSearchAggregationBucketKey], UnsetType] = unset,
        template_variables_name: Union[List[NotebookSearchAggregationBucketKey], UnsetType] = unset,
        type: Union[List[NotebookSearchAggregationBucketKey], UnsetType] = unset,
        **kwargs,
    ):
        """
        Aggregations of notebook search results.

        :param author: Aggregation by author.
        :type author: [NotebookSearchAggregationBucketMultiKey], optional

        :param tags: Aggregation by tags.
        :type tags: [NotebookSearchAggregationBucketKey], optional

        :param template_variables_name: Aggregation by template variable names.
        :type template_variables_name: [NotebookSearchAggregationBucketKey], optional

        :param type: Aggregation by notebook type.
        :type type: [NotebookSearchAggregationBucketKey], optional
        """
        if author is not unset:
            kwargs["author"] = author
        if tags is not unset:
            kwargs["tags"] = tags
        if template_variables_name is not unset:
            kwargs["template_variables_name"] = template_variables_name
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
