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
    from datadog_api_client.v2.model.aggregated_waterfall_performance_criteria import (
        AggregatedWaterfallPerformanceCriteria,
    )
    from datadog_api_client.v2.model.aggregated_long_tasks_by_invoker_type import AggregatedLongTasksByInvokerType


class AggregatedLongTasksResponseAttributes(ModelNormal):
    validations = {
        "view_count": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aggregated_waterfall_performance_criteria import (
            AggregatedWaterfallPerformanceCriteria,
        )
        from datadog_api_client.v2.model.aggregated_long_tasks_by_invoker_type import AggregatedLongTasksByInvokerType

        return {
            "application_id": (str,),
            "criteria": (AggregatedWaterfallPerformanceCriteria,),
            "_from": (int,),
            "long_tasks_by_invoker_type": ([AggregatedLongTasksByInvokerType],),
            "sampled_view_ids": ([str],),
            "to": (int,),
            "view_count": (int,),
            "view_name": (str,),
        }

    attribute_map = {
        "application_id": "application_id",
        "criteria": "criteria",
        "_from": "from",
        "long_tasks_by_invoker_type": "long_tasks_by_invoker_type",
        "sampled_view_ids": "sampled_view_ids",
        "to": "to",
        "view_count": "view_count",
        "view_name": "view_name",
    }

    def __init__(
        self_,
        application_id: str,
        _from: int,
        long_tasks_by_invoker_type: List[AggregatedLongTasksByInvokerType],
        sampled_view_ids: List[str],
        to: int,
        view_count: int,
        view_name: str,
        criteria: Union[AggregatedWaterfallPerformanceCriteria, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an aggregated long tasks response.

        :param application_id: The RUM application ID that was analyzed.
        :type application_id: str

        :param criteria: Performance criteria to filter view instances by a metric threshold.
        :type criteria: AggregatedWaterfallPerformanceCriteria, optional

        :param _from: Start of the analyzed time range as a Unix timestamp in seconds.
        :type _from: int

        :param long_tasks_by_invoker_type: Long task statistics grouped by invoker type, sorted by impact score descending.
        :type long_tasks_by_invoker_type: [AggregatedLongTasksByInvokerType]

        :param sampled_view_ids: List of RUM view IDs sampled for this aggregation, capped at 50.
        :type sampled_view_ids: [str]

        :param to: End of the analyzed time range as a Unix timestamp in seconds.
        :type to: int

        :param view_count: Number of view instances included in the analysis.
        :type view_count: int

        :param view_name: The RUM view name that was analyzed.
        :type view_name: str
        """
        if criteria is not unset:
            kwargs["criteria"] = criteria
        super().__init__(kwargs)

        self_.application_id = application_id
        self_._from = _from
        self_.long_tasks_by_invoker_type = long_tasks_by_invoker_type
        self_.sampled_view_ids = sampled_view_ids
        self_.to = to
        self_.view_count = view_count
        self_.view_name = view_name
