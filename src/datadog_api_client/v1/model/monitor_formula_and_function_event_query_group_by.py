# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.monitor_formula_and_function_event_query_group_by_sort import (
        MonitorFormulaAndFunctionEventQueryGroupBySort,
    )


class MonitorFormulaAndFunctionEventQueryGroupBy(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.monitor_formula_and_function_event_query_group_by_sort import (
            MonitorFormulaAndFunctionEventQueryGroupBySort,
        )

        return {
            "facet": (str,),
            "limit": (int,),
            "sort": (MonitorFormulaAndFunctionEventQueryGroupBySort,),
        }

    attribute_map = {
        "facet": "facet",
        "limit": "limit",
        "sort": "sort",
    }

    def __init__(
        self_,
        facet: str,
        limit: Union[int, UnsetType] = unset,
        sort: Union[MonitorFormulaAndFunctionEventQueryGroupBySort, UnsetType] = unset,
        **kwargs,
    ):
        """
        List of objects used to group by.

        :param facet: Event facet.
        :type facet: str

        :param limit: Number of groups to return.
        :type limit: int, optional

        :param sort: Options for sorting group by results.
        :type sort: MonitorFormulaAndFunctionEventQueryGroupBySort, optional
        """
        if limit is not unset:
            kwargs["limit"] = limit
        if sort is not unset:
            kwargs["sort"] = sort
        super().__init__(kwargs)

        self_.facet = facet
