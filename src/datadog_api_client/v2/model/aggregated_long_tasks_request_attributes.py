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
    from datadog_api_client.v2.model.aggregated_waterfall_performance_criteria import (
        AggregatedWaterfallPerformanceCriteria,
    )


class AggregatedLongTasksRequestAttributes(ModelNormal):
    validations = {
        "sample_size": {
            "inclusive_maximum": 500,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aggregated_waterfall_performance_criteria import (
            AggregatedWaterfallPerformanceCriteria,
        )

        return {
            "application_id": (str,),
            "criteria": (AggregatedWaterfallPerformanceCriteria,),
            "filter": (str,),
            "_from": (int,),
            "sample_size": (int,),
            "to": (int,),
            "view_name": (str,),
        }

    attribute_map = {
        "application_id": "application_id",
        "criteria": "criteria",
        "filter": "filter",
        "_from": "from",
        "sample_size": "sample_size",
        "to": "to",
        "view_name": "view_name",
    }

    def __init__(
        self_,
        application_id: str,
        _from: int,
        sample_size: int,
        to: int,
        view_name: str,
        criteria: Union[AggregatedWaterfallPerformanceCriteria, UnsetType] = unset,
        filter: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for an aggregated long tasks query.

        :param application_id: The RUM application ID to analyze.
        :type application_id: str

        :param criteria: Performance criteria to filter view instances by a metric threshold.
        :type criteria: AggregatedWaterfallPerformanceCriteria, optional

        :param filter: RUM query string to filter events (for example, @session.type:user @geo.country:US).
        :type filter: str, optional

        :param _from: Start of the time range as a Unix timestamp in seconds.
        :type _from: int

        :param sample_size: Number of view instances to sample, between 1 and 500.
        :type sample_size: int

        :param to: End of the time range as a Unix timestamp in seconds.
        :type to: int

        :param view_name: The RUM view name to analyze (for example, /account/login).
        :type view_name: str
        """
        if criteria is not unset:
            kwargs["criteria"] = criteria
        if filter is not unset:
            kwargs["filter"] = filter
        super().__init__(kwargs)

        self_.application_id = application_id
        self_._from = _from
        self_.sample_size = sample_size
        self_.to = to
        self_.view_name = view_name
