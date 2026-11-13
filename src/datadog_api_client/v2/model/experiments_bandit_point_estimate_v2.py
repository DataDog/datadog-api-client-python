# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_bandit_confidence_interval_v2 import (
        ExperimentsBanditConfidenceIntervalV2,
    )


class ExperimentsBanditPointEstimateV2(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_bandit_confidence_interval_v2 import (
            ExperimentsBanditConfidenceIntervalV2,
        )

        return {
            "confidence_interval": (ExperimentsBanditConfidenceIntervalV2,),
            "data_as_of": (datetime, none_type),
            "feature_flag_variant_id": (UUID,),
            "point_estimate": (float,),
            "refresh_id": (UUID,),
            "results_last_updated": (datetime,),
            "variant_key": (str, none_type),
        }

    attribute_map = {
        "confidence_interval": "confidence_interval",
        "data_as_of": "data_as_of",
        "feature_flag_variant_id": "feature_flag_variant_id",
        "point_estimate": "point_estimate",
        "refresh_id": "refresh_id",
        "results_last_updated": "results_last_updated",
        "variant_key": "variant_key",
    }

    def __init__(
        self_,
        confidence_interval: ExperimentsBanditConfidenceIntervalV2,
        data_as_of: Union[datetime, none_type],
        feature_flag_variant_id: UUID,
        point_estimate: float,
        refresh_id: UUID,
        results_last_updated: datetime,
        variant_key: Union[str, none_type],
        **kwargs,
    ):
        """
        An arm's point estimate from one saved refresh.

        :param confidence_interval: A central interval around point_estimate at confidence_level.
        :type confidence_interval: ExperimentsBanditConfidenceIntervalV2

        :param data_as_of: The latest warehouse data the refresh read.
        :type data_as_of: datetime, none_type

        :param feature_flag_variant_id: The arm's variant ID on the flag.
        :type feature_flag_variant_id: UUID

        :param point_estimate: The arm's estimated mean of the metric, in the metric's units.
        :type point_estimate: float

        :param refresh_id: The refresh the estimate comes from.
        :type refresh_id: UUID

        :param results_last_updated: When the refresh saved its results.
        :type results_last_updated: datetime

        :param variant_key: The arm's variant key.
        :type variant_key: str, none_type
        """
        super().__init__(kwargs)

        self_.confidence_interval = confidence_interval
        self_.data_as_of = data_as_of
        self_.feature_flag_variant_id = feature_flag_variant_id
        self_.point_estimate = point_estimate
        self_.refresh_id = refresh_id
        self_.results_last_updated = results_last_updated
        self_.variant_key = variant_key
