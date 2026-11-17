# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ExperimentsBanditBayesianPriorV2(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "arm_standard_deviation": (float,),
            "grand_mean": (float,),
            "grand_mean_standard_deviation": (float,),
        }

    attribute_map = {
        "arm_standard_deviation": "arm_standard_deviation",
        "grand_mean": "grand_mean",
        "grand_mean_standard_deviation": "grand_mean_standard_deviation",
    }

    def __init__(
        self_, arm_standard_deviation: float, grand_mean: float, grand_mean_standard_deviation: float, **kwargs
    ):
        """
        The prior the bandit's estimates start from.

        :param arm_standard_deviation: Prior standard deviation of each arm's mean around the shared mean.
        :type arm_standard_deviation: float

        :param grand_mean: Prior mean of the shared mean of the arms, in the metric's units.
        :type grand_mean: float

        :param grand_mean_standard_deviation: Prior standard deviation of the shared mean of the arms.
        :type grand_mean_standard_deviation: float
        """
        super().__init__(kwargs)

        self_.arm_standard_deviation = arm_standard_deviation
        self_.grand_mean = grand_mean
        self_.grand_mean_standard_deviation = grand_mean_standard_deviation
