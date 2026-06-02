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
    from datadog_api_client.v2.model.signals_problems_detections import SignalsProblemsDetections
    from datadog_api_client.v2.model.signals_problems_sample_metadata import SignalsProblemsSampleMetadata


class AggregatedSignalsProblemsResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aggregated_waterfall_performance_criteria import (
            AggregatedWaterfallPerformanceCriteria,
        )
        from datadog_api_client.v2.model.signals_problems_detections import SignalsProblemsDetections
        from datadog_api_client.v2.model.signals_problems_sample_metadata import SignalsProblemsSampleMetadata

        return {
            "application_id": (str,),
            "criteria": (AggregatedWaterfallPerformanceCriteria,),
            "_from": (int,),
            "problem_detections": (SignalsProblemsDetections,),
            "sample_metadata": (SignalsProblemsSampleMetadata,),
            "to": (int,),
            "view_name": (str,),
        }

    attribute_map = {
        "application_id": "application_id",
        "criteria": "criteria",
        "_from": "from",
        "problem_detections": "problem_detections",
        "sample_metadata": "sample_metadata",
        "to": "to",
        "view_name": "view_name",
    }

    def __init__(
        self_,
        application_id: str,
        _from: int,
        problem_detections: SignalsProblemsDetections,
        sample_metadata: SignalsProblemsSampleMetadata,
        to: int,
        view_name: str,
        criteria: Union[AggregatedWaterfallPerformanceCriteria, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an aggregated signals and problems response.

        :param application_id: The RUM application ID that was analyzed.
        :type application_id: str

        :param criteria: Performance criteria to filter view instances by a metric threshold.
        :type criteria: AggregatedWaterfallPerformanceCriteria, optional

        :param _from: Start of the analyzed time range as a Unix timestamp in seconds.
        :type _from: int

        :param problem_detections: Grouped detection results by detection type.
        :type problem_detections: SignalsProblemsDetections

        :param sample_metadata: Metadata about the sampling quality for a signals and problems query.
        :type sample_metadata: SignalsProblemsSampleMetadata

        :param to: End of the analyzed time range as a Unix timestamp in seconds.
        :type to: int

        :param view_name: The RUM view name that was analyzed.
        :type view_name: str
        """
        if criteria is not unset:
            kwargs["criteria"] = criteria
        super().__init__(kwargs)

        self_.application_id = application_id
        self_._from = _from
        self_.problem_detections = problem_detections
        self_.sample_metadata = sample_metadata
        self_.to = to
        self_.view_name = view_name
