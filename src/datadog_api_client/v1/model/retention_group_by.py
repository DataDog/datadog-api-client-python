# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.retention_group_by_sort import RetentionGroupBySort
    from datadog_api_client.v1.model.retention_group_by_target import RetentionGroupByTarget


class RetentionGroupBy(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.retention_group_by_sort import RetentionGroupBySort
        from datadog_api_client.v1.model.retention_group_by_target import RetentionGroupByTarget

        return {
            "facet": (str,),
            "limit": (int,),
            "should_exclude_missing": (bool,),
            "sort": (RetentionGroupBySort,),
            "source": (str,),
            "target": (RetentionGroupByTarget,),
        }

    attribute_map = {
        "facet": "facet",
        "limit": "limit",
        "should_exclude_missing": "should_exclude_missing",
        "sort": "sort",
        "source": "source",
        "target": "target",
    }

    def __init__(
        self_,
        facet: str,
        target: RetentionGroupByTarget,
        limit: Union[int, UnsetType] = unset,
        should_exclude_missing: Union[bool, UnsetType] = unset,
        sort: Union[RetentionGroupBySort, UnsetType] = unset,
        source: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Group by configuration for retention queries.

        :param facet: Facet to group by.
        :type facet: str

        :param limit: Maximum number of groups.
        :type limit: int, optional

        :param should_exclude_missing: Whether to exclude missing values.
        :type should_exclude_missing: bool, optional

        :param sort: Sort configuration for retention group by.
        :type sort: RetentionGroupBySort, optional

        :param source: Source field.
        :type source: str, optional

        :param target: Target for retention group by.
        :type target: RetentionGroupByTarget
        """
        if limit is not unset:
            kwargs["limit"] = limit
        if should_exclude_missing is not unset:
            kwargs["should_exclude_missing"] = should_exclude_missing
        if sort is not unset:
            kwargs["sort"] = sort
        if source is not unset:
            kwargs["source"] = source
        super().__init__(kwargs)

        self_.facet = facet
        self_.target = target
