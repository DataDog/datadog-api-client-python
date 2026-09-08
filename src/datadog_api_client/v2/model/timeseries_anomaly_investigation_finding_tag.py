# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_influence_type import (
        TimeseriesAnomalyInvestigationInfluenceType,
    )
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_finding_synonym import (
        TimeseriesAnomalyInvestigationFindingSynonym,
    )


class TimeseriesAnomalyInvestigationFindingTag(ModelNormal):
    validations = {
        "rating": {
            "inclusive_maximum": 5,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_influence_type import (
            TimeseriesAnomalyInvestigationInfluenceType,
        )
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_finding_synonym import (
            TimeseriesAnomalyInvestigationFindingSynonym,
        )

        return {
            "influence_type": (TimeseriesAnomalyInvestigationInfluenceType,),
            "key": (str,),
            "rating": (float,),
            "synonyms": ([TimeseriesAnomalyInvestigationFindingSynonym],),
            "values": ([str],),
        }

    attribute_map = {
        "influence_type": "influence_type",
        "key": "key",
        "rating": "rating",
        "synonyms": "synonyms",
        "values": "values",
    }

    def __init__(
        self_,
        influence_type: TimeseriesAnomalyInvestigationInfluenceType,
        key: str,
        rating: float,
        synonyms: List[TimeseriesAnomalyInvestigationFindingSynonym],
        values: List[str],
        **kwargs,
    ):
        """
        Structured tag evidence for an influential-tag finding.

        :param influence_type: Kind of influence a tag has on a series.
        :type influence_type: TimeseriesAnomalyInvestigationInfluenceType

        :param key: Influential tag key.
        :type key: str

        :param rating: Influence rating from 1 through 5.
        :type rating: float

        :param synonyms: Tags grouped with this tag by Variation of Influence synonym analysis.
        :type synonyms: [TimeseriesAnomalyInvestigationFindingSynonym]

        :param values: Influential values for the tag key.
        :type values: [str]
        """
        super().__init__(kwargs)

        self_.influence_type = influence_type
        self_.key = key
        self_.rating = rating
        self_.synonyms = synonyms
        self_.values = values
