# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_bandit_nullable_confidence_interval_v2 import (
        ExperimentsBanditNullableConfidenceIntervalV2,
    )
    from datadog_api_client.v2.model.experiments_bandit_arm_data_status import ExperimentsBanditArmDataStatus
    from datadog_api_client.v2.model.experiments_bandit_posterior_unavailable_reason import (
        ExperimentsBanditPosteriorUnavailableReason,
    )


class ExperimentsBanditVariantResultV2(ModelNormal):
    validations = {
        "probability_of_being_optimal": {
            "inclusive_maximum": 1,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_bandit_nullable_confidence_interval_v2 import (
            ExperimentsBanditNullableConfidenceIntervalV2,
        )
        from datadog_api_client.v2.model.experiments_bandit_arm_data_status import ExperimentsBanditArmDataStatus
        from datadog_api_client.v2.model.experiments_bandit_posterior_unavailable_reason import (
            ExperimentsBanditPosteriorUnavailableReason,
        )

        return {
            "confidence_interval": (ExperimentsBanditNullableConfidenceIntervalV2,),
            "data_status": (ExperimentsBanditArmDataStatus,),
            "feature_flag_variant_id": (UUID,),
            "mature_observations": (int,),
            "point_estimate": (float, none_type),
            "posterior_unavailable_reason": (ExperimentsBanditPosteriorUnavailableReason,),
            "probability_of_being_optimal": (float, none_type),
            "variant_key": (str, none_type),
        }

    attribute_map = {
        "confidence_interval": "confidence_interval",
        "data_status": "data_status",
        "feature_flag_variant_id": "feature_flag_variant_id",
        "mature_observations": "mature_observations",
        "point_estimate": "point_estimate",
        "posterior_unavailable_reason": "posterior_unavailable_reason",
        "probability_of_being_optimal": "probability_of_being_optimal",
        "variant_key": "variant_key",
    }

    def __init__(
        self_,
        confidence_interval: Union[ExperimentsBanditNullableConfidenceIntervalV2, none_type],
        feature_flag_variant_id: UUID,
        mature_observations: int,
        point_estimate: Union[float, none_type],
        probability_of_being_optimal: Union[float, none_type],
        variant_key: Union[str, none_type],
        data_status: Union[ExperimentsBanditArmDataStatus, UnsetType] = unset,
        posterior_unavailable_reason: Union[ExperimentsBanditPosteriorUnavailableReason, UnsetType] = unset,
        **kwargs,
    ):
        """
        An arm's estimates from the latest saved refresh.

        :param confidence_interval: A central interval around point_estimate at confidence_level. Null when the estimate is unavailable.
        :type confidence_interval: ExperimentsBanditNullableConfidenceIntervalV2, none_type

        :param data_status: Where the arm's reward variance came from, or why it's unavailable.
        :type data_status: ExperimentsBanditArmDataStatus, optional

        :param feature_flag_variant_id: The arm's variant ID on the flag.
        :type feature_flag_variant_id: UUID

        :param mature_observations: The arm's valid observations whose aggregation window has closed. The estimate uses these.
        :type mature_observations: int

        :param point_estimate: The arm's estimated mean of the metric, in the metric's units. It isn't a lift.
        :type point_estimate: float, none_type

        :param posterior_unavailable_reason: Why the arm's estimate and interval are unavailable. Absent when they are available.
        :type posterior_unavailable_reason: ExperimentsBanditPosteriorUnavailableReason, optional

        :param probability_of_being_optimal: The probability that this arm is the best.
        :type probability_of_being_optimal: float, none_type

        :param variant_key: The arm's variant key.
        :type variant_key: str, none_type
        """
        if data_status is not unset:
            kwargs["data_status"] = data_status
        if posterior_unavailable_reason is not unset:
            kwargs["posterior_unavailable_reason"] = posterior_unavailable_reason
        super().__init__(kwargs)

        self_.confidence_interval = confidence_interval
        self_.feature_flag_variant_id = feature_flag_variant_id
        self_.mature_observations = mature_observations
        self_.point_estimate = point_estimate
        self_.probability_of_being_optimal = probability_of_being_optimal
        self_.variant_key = variant_key
