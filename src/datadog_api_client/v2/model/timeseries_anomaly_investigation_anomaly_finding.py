# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_anomaly_finding_type import (
        TimeseriesAnomalyInvestigationAnomalyFindingType,
    )


class TimeseriesAnomalyInvestigationAnomalyFinding(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_anomaly_finding_type import (
            TimeseriesAnomalyInvestigationAnomalyFindingType,
        )

        return {
            "description": (str,),
            "headline": (str,),
            "type": (TimeseriesAnomalyInvestigationAnomalyFindingType,),
        }

    attribute_map = {
        "description": "description",
        "headline": "headline",
        "type": "type",
    }

    def __init__(
        self_, description: str, headline: str, type: TimeseriesAnomalyInvestigationAnomalyFindingType, **kwargs
    ):
        """
        Finding that describes the anomaly when completed analysis produces no displayable influential tags.

        :param description: Deterministic explanation of the finding.
        :type description: str

        :param headline: Concise, deterministic finding title.
        :type headline: str

        :param type: Finding category for an anomaly without a displayable influential tag.
        :type type: TimeseriesAnomalyInvestigationAnomalyFindingType
        """
        super().__init__(kwargs)

        self_.description = description
        self_.headline = headline
        self_.type = type
