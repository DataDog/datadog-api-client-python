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
    from datadog_api_client.v1_20270101.model.formula_and_function_event_query_group_by_sort import (
        FormulaAndFunctionEventQueryGroupBySort,
    )
    from datadog_api_client.v1_20270101.model.graph_target import GraphTarget
    from datadog_api_client.v1_20270101.model.graph_target_node import GraphTargetNode
    from datadog_api_client.v1_20270101.model.graph_target_path import GraphTargetPath


class FormulaGraphQueryGroupByItems(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.formula_and_function_event_query_group_by_sort import (
            FormulaAndFunctionEventQueryGroupBySort,
        )
        from datadog_api_client.v1_20270101.model.graph_target import GraphTarget

        return {
            "facet": (str,),
            "limit": (float,),
            "should_exclude_missing": (bool,),
            "sort": (FormulaAndFunctionEventQueryGroupBySort,),
            "source": (str,),
            "target": (GraphTarget,),
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
        limit: Union[float, UnsetType] = unset,
        should_exclude_missing: Union[bool, UnsetType] = unset,
        sort: Union[FormulaAndFunctionEventQueryGroupBySort, UnsetType] = unset,
        source: Union[str, UnsetType] = unset,
        target: Union[GraphTarget, GraphTargetNode, GraphTargetPath, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param facet: Test-only generated schema for the dashboard versioning proof of concept.
        :type facet: str

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float, optional

        :param should_exclude_missing: Test-only generated schema for the dashboard versioning proof of concept.
        :type should_exclude_missing: bool, optional

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: FormulaAndFunctionEventQueryGroupBySort, optional

        :param source: Test-only generated schema for the dashboard versioning proof of concept.
        :type source: str, optional

        :param target: Test-only generated schema for the dashboard versioning proof of concept.
        :type target: GraphTarget, optional
        """
        if limit is not unset:
            kwargs["limit"] = limit
        if should_exclude_missing is not unset:
            kwargs["should_exclude_missing"] = should_exclude_missing
        if sort is not unset:
            kwargs["sort"] = sort
        if source is not unset:
            kwargs["source"] = source
        if target is not unset:
            kwargs["target"] = target
        super().__init__(kwargs)

        self_.facet = facet
