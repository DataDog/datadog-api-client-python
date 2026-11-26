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
    from datadog_api_client.v1_20270101.model.formula_and_function_event_query_group_by_sort import (
        FormulaAndFunctionEventQueryGroupBySort,
    )


class FormulaAndFunctionEventQueryGroupByFields(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.formula_and_function_event_query_group_by_sort import (
            FormulaAndFunctionEventQueryGroupBySort,
        )

        return {
            "fields": ([str],),
            "limit": (float,),
            "should_exclude_missing": (bool,),
            "sort": (FormulaAndFunctionEventQueryGroupBySort,),
        }

    attribute_map = {
        "fields": "fields",
        "limit": "limit",
        "should_exclude_missing": "should_exclude_missing",
        "sort": "sort",
    }

    def __init__(
        self_,
        fields: List[str],
        limit: Union[float, UnsetType] = unset,
        should_exclude_missing: Union[bool, UnsetType] = unset,
        sort: Union[FormulaAndFunctionEventQueryGroupBySort, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param fields: Test-only generated schema for the dashboard versioning proof of concept.
        :type fields: [str]

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float, optional

        :param should_exclude_missing: Test-only generated schema for the dashboard versioning proof of concept.
        :type should_exclude_missing: bool, optional

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: FormulaAndFunctionEventQueryGroupBySort, optional
        """
        if limit is not unset:
            kwargs["limit"] = limit
        if should_exclude_missing is not unset:
            kwargs["should_exclude_missing"] = should_exclude_missing
        if sort is not unset:
            kwargs["sort"] = sort
        super().__init__(kwargs)

        self_.fields = fields
