# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.apm_recommendations_stream_query_data_source import (
        ApmRecommendationsStreamQueryDataSource,
    )
    from datadog_api_client.v1.model.apm_recommendations_stream_query20270101_group_by import (
        ApmRecommendationsStreamQuery20270101GroupBy,
    )
    from datadog_api_client.v1_20270101.model.apm_recommendations_stream_query20270101_sort import (
        ApmRecommendationsStreamQuery20270101Sort,
    )
    from datadog_api_client.v1_20270101.model.list_stream_sort import ListStreamSort


class ApmRecommendationsStreamQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.apm_recommendations_stream_query_data_source import (
            ApmRecommendationsStreamQueryDataSource,
        )
        from datadog_api_client.v1.model.apm_recommendations_stream_query20270101_group_by import (
            ApmRecommendationsStreamQuery20270101GroupBy,
        )
        from datadog_api_client.v1_20270101.model.apm_recommendations_stream_query20270101_sort import (
            ApmRecommendationsStreamQuery20270101Sort,
        )

        return {
            "cross_org_uuids": ([str],),
            "custom_service_tags": ([str],),
            "data_source": (ApmRecommendationsStreamQueryDataSource,),
            "env": (str,),
            "group_by": (ApmRecommendationsStreamQuery20270101GroupBy,),
            "indexes": ([str],),
            "priorities": ([str],),
            "query_string": (str,),
            "recommendation_types": ([str],),
            "services": ([str],),
            "sort": (ApmRecommendationsStreamQuery20270101Sort,),
            "statuses": ([str],),
            "teams": ([str],),
        }

    attribute_map = {
        "cross_org_uuids": "cross_org_uuids",
        "custom_service_tags": "custom_service_tags",
        "data_source": "data_source",
        "env": "env",
        "group_by": "group_by",
        "indexes": "indexes",
        "priorities": "priorities",
        "query_string": "query_string",
        "recommendation_types": "recommendation_types",
        "services": "services",
        "sort": "sort",
        "statuses": "statuses",
        "teams": "teams",
    }

    def __init__(
        self_,
        data_source: ApmRecommendationsStreamQueryDataSource,
        query_string: str,
        cross_org_uuids: Union[List[str], UnsetType] = unset,
        custom_service_tags: Union[List[str], UnsetType] = unset,
        env: Union[str, UnsetType] = unset,
        group_by: Union[ApmRecommendationsStreamQuery20270101GroupBy, List[Any], List[Any], UnsetType] = unset,
        indexes: Union[List[str], UnsetType] = unset,
        priorities: Union[List[str], UnsetType] = unset,
        recommendation_types: Union[List[str], UnsetType] = unset,
        services: Union[List[str], UnsetType] = unset,
        sort: Union[ApmRecommendationsStreamQuery20270101Sort, ListStreamSort, List[ListStreamSort], UnsetType] = unset,
        statuses: Union[List[str], UnsetType] = unset,
        teams: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param cross_org_uuids: Test-only generated schema for the dashboard versioning proof of concept.
        :type cross_org_uuids: [str], optional

        :param custom_service_tags: Test-only generated schema for the dashboard versioning proof of concept.
        :type custom_service_tags: [str], optional

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: ApmRecommendationsStreamQueryDataSource

        :param env: Test-only generated schema for the dashboard versioning proof of concept.
        :type env: str, optional

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: ApmRecommendationsStreamQuery20270101GroupBy, optional

        :param indexes: Test-only generated schema for the dashboard versioning proof of concept.
        :type indexes: [str], optional

        :param priorities: Test-only generated schema for the dashboard versioning proof of concept.
        :type priorities: [str], optional

        :param query_string: Test-only generated schema for the dashboard versioning proof of concept.
        :type query_string: str

        :param recommendation_types: Test-only generated schema for the dashboard versioning proof of concept.
        :type recommendation_types: [str], optional

        :param services: Test-only generated schema for the dashboard versioning proof of concept.
        :type services: [str], optional

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: ApmRecommendationsStreamQuery20270101Sort, optional

        :param statuses: Test-only generated schema for the dashboard versioning proof of concept.
        :type statuses: [str], optional

        :param teams: Test-only generated schema for the dashboard versioning proof of concept.
        :type teams: [str], optional
        """
        if cross_org_uuids is not unset:
            kwargs["cross_org_uuids"] = cross_org_uuids
        if custom_service_tags is not unset:
            kwargs["custom_service_tags"] = custom_service_tags
        if env is not unset:
            kwargs["env"] = env
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if indexes is not unset:
            kwargs["indexes"] = indexes
        if priorities is not unset:
            kwargs["priorities"] = priorities
        if recommendation_types is not unset:
            kwargs["recommendation_types"] = recommendation_types
        if services is not unset:
            kwargs["services"] = services
        if sort is not unset:
            kwargs["sort"] = sort
        if statuses is not unset:
            kwargs["statuses"] = statuses
        if teams is not unset:
            kwargs["teams"] = teams
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.query_string = query_string
