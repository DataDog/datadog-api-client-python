# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_bandit_daily_traffic_v2 import ExperimentsBanditDailyTrafficV2
    from datadog_api_client.v2.model.experiments_bandit_observation_counts_v2 import (
        ExperimentsBanditObservationCountsV2,
    )
    from datadog_api_client.v2.model.experiments_bandit_traffic_variant_v2 import ExperimentsBanditTrafficVariantV2


class ExperimentsBanditTrafficSummaryV2DTODataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_bandit_daily_traffic_v2 import ExperimentsBanditDailyTrafficV2
        from datadog_api_client.v2.model.experiments_bandit_observation_counts_v2 import (
            ExperimentsBanditObservationCountsV2,
        )
        from datadog_api_client.v2.model.experiments_bandit_traffic_variant_v2 import ExperimentsBanditTrafficVariantV2

        return {
            "daily": ([ExperimentsBanditDailyTrafficV2],),
            "data_as_of": (datetime, none_type),
            "observation_counts": (ExperimentsBanditObservationCountsV2,),
            "refresh_id": (UUID, none_type),
            "total_subjects": (int,),
            "variants": ([ExperimentsBanditTrafficVariantV2],),
        }

    attribute_map = {
        "daily": "daily",
        "data_as_of": "data_as_of",
        "observation_counts": "observation_counts",
        "refresh_id": "refresh_id",
        "total_subjects": "total_subjects",
        "variants": "variants",
    }

    def __init__(
        self_,
        daily: List[ExperimentsBanditDailyTrafficV2],
        data_as_of: Union[datetime, none_type],
        observation_counts: Union[ExperimentsBanditObservationCountsV2, none_type],
        refresh_id: Union[UUID, none_type],
        total_subjects: int,
        variants: List[ExperimentsBanditTrafficVariantV2],
        **kwargs,
    ):
        """
        What the bandit has observed, as of its latest saved refresh.

        :param daily: Valid observations per arm on the UTC day of their anchor time, for each day from the bandit's start to the data cutoff that overlaps the requested range. Days without any have zero counts. Empty before the first saved refresh.
        :type daily: [ExperimentsBanditDailyTrafficV2]

        :param data_as_of: The latest warehouse data the latest saved refresh read.
        :type data_as_of: datetime, none_type

        :param observation_counts: How many observations the latest saved refresh saw, whatever the range. Null when its counts can't be read.
        :type observation_counts: ExperimentsBanditObservationCountsV2, none_type

        :param refresh_id: The latest refresh that saved results. The counts come from it.
        :type refresh_id: UUID, none_type

        :param total_subjects: Distinct subjects with a valid observation, whatever the range.
        :type total_subjects: int

        :param variants: One row per arm, whatever the range.
        :type variants: [ExperimentsBanditTrafficVariantV2]
        """
        super().__init__(kwargs)

        self_.daily = daily
        self_.data_as_of = data_as_of
        self_.observation_counts = observation_counts
        self_.refresh_id = refresh_id
        self_.total_subjects = total_subjects
        self_.variants = variants
