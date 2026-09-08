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
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_finding_tag import (
        TimeseriesAnomalyInvestigationFindingTag,
    )
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_influential_tag_finding_type import (
        TimeseriesAnomalyInvestigationInfluentialTagFindingType,
    )


class TimeseriesAnomalyInvestigationInfluentialTagFinding(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_finding_tag import (
            TimeseriesAnomalyInvestigationFindingTag,
        )
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_influential_tag_finding_type import (
            TimeseriesAnomalyInvestigationInfluentialTagFindingType,
        )

        return {
            "description": (str,),
            "headline": (str,),
            "tag": (TimeseriesAnomalyInvestigationFindingTag,),
            "type": (TimeseriesAnomalyInvestigationInfluentialTagFindingType,),
        }

    attribute_map = {
        "description": "description",
        "headline": "headline",
        "tag": "tag",
        "type": "type",
    }

    def __init__(
        self_,
        description: str,
        headline: str,
        tag: TimeseriesAnomalyInvestigationFindingTag,
        type: TimeseriesAnomalyInvestigationInfluentialTagFindingType,
        **kwargs,
    ):
        """
        Finding that attributes an anomaly to an influential tag.

        :param description: Deterministic explanation of the finding.
        :type description: str

        :param headline: Concise, deterministic finding title.
        :type headline: str

        :param tag: Structured tag evidence for an influential-tag finding.
        :type tag: TimeseriesAnomalyInvestigationFindingTag

        :param type: Finding category for an influential tag.
        :type type: TimeseriesAnomalyInvestigationInfluentialTagFindingType
        """
        super().__init__(kwargs)

        self_.description = description
        self_.headline = headline
        self_.tag = tag
        self_.type = type
