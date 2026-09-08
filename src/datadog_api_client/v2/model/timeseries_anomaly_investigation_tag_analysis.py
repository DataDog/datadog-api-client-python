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
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_tag_analysis_status import (
        TimeseriesAnomalyInvestigationTagAnalysisStatus,
    )


class TimeseriesAnomalyInvestigationTagAnalysis(ModelNormal):
    validations = {
        "tag_keys_analyzed": {
            "inclusive_minimum": 0,
        },
        "tag_values_analyzed": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_tag_analysis_status import (
            TimeseriesAnomalyInvestigationTagAnalysisStatus,
        )

        return {
            "analyzed_tag_keys": ([str],),
            "status": (TimeseriesAnomalyInvestigationTagAnalysisStatus,),
            "tag_keys_analyzed": (int,),
            "tag_values_analyzed": (int,),
        }

    attribute_map = {
        "analyzed_tag_keys": "analyzed_tag_keys",
        "status": "status",
        "tag_keys_analyzed": "tag_keys_analyzed",
        "tag_values_analyzed": "tag_values_analyzed",
    }

    def __init__(
        self_,
        status: TimeseriesAnomalyInvestigationTagAnalysisStatus,
        analyzed_tag_keys: Union[List[str], UnsetType] = unset,
        tag_keys_analyzed: Union[int, UnsetType] = unset,
        tag_values_analyzed: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Summary of optional influential-tag enrichment. Count and key fields are present only when analysis completes; enrichment availability does not affect completion of the investigation result.

        :param analyzed_tag_keys: Tag keys analyzed. Present only when analysis completes.
        :type analyzed_tag_keys: [str], optional

        :param status: Outcome of optional influential-tag enrichment.
        :type status: TimeseriesAnomalyInvestigationTagAnalysisStatus

        :param tag_keys_analyzed: Number of tag keys analyzed. Present only when analysis completes.
        :type tag_keys_analyzed: int, optional

        :param tag_values_analyzed: Number of tag values analyzed. Present only when analysis completes.
        :type tag_values_analyzed: int, optional
        """
        if analyzed_tag_keys is not unset:
            kwargs["analyzed_tag_keys"] = analyzed_tag_keys
        if tag_keys_analyzed is not unset:
            kwargs["tag_keys_analyzed"] = tag_keys_analyzed
        if tag_values_analyzed is not unset:
            kwargs["tag_values_analyzed"] = tag_values_analyzed
        super().__init__(kwargs)

        self_.status = status
