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
    from datadog_api_client.v1_20270101.model.recommendations_stream_query_data_source import (
        RecommendationsStreamQueryDataSource,
    )
    from datadog_api_client.v1_20270101.model.recommendations_stream_query20270101_sort import (
        RecommendationsStreamQuery20270101Sort,
    )
    from datadog_api_client.v1_20270101.model.list_stream_sort import ListStreamSort


class RecommendationsStreamQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.recommendations_stream_query_data_source import (
            RecommendationsStreamQueryDataSource,
        )
        from datadog_api_client.v1_20270101.model.recommendations_stream_query20270101_sort import (
            RecommendationsStreamQuery20270101Sort,
        )

        return {
            "cross_org_uuids": ([str],),
            "data_source": (RecommendationsStreamQueryDataSource,),
            "indexes": ([str],),
            "query_string": (str,),
            "sort": (RecommendationsStreamQuery20270101Sort,),
        }

    attribute_map = {
        "cross_org_uuids": "cross_org_uuids",
        "data_source": "data_source",
        "indexes": "indexes",
        "query_string": "query_string",
        "sort": "sort",
    }

    def __init__(
        self_,
        data_source: RecommendationsStreamQueryDataSource,
        query_string: str,
        cross_org_uuids: Union[List[str], UnsetType] = unset,
        indexes: Union[List[str], UnsetType] = unset,
        sort: Union[RecommendationsStreamQuery20270101Sort, ListStreamSort, List[ListStreamSort], UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param cross_org_uuids: Test-only generated schema for the dashboard versioning proof of concept.
        :type cross_org_uuids: [str], optional

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: RecommendationsStreamQueryDataSource

        :param indexes: Test-only generated schema for the dashboard versioning proof of concept.
        :type indexes: [str], optional

        :param query_string: Test-only generated schema for the dashboard versioning proof of concept.
        :type query_string: str

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: RecommendationsStreamQuery20270101Sort, optional
        """
        if cross_org_uuids is not unset:
            kwargs["cross_org_uuids"] = cross_org_uuids
        if indexes is not unset:
            kwargs["indexes"] = indexes
        if sort is not unset:
            kwargs["sort"] = sort
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.query_string = query_string
