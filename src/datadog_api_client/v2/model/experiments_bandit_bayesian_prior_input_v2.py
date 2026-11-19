# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ExperimentsBanditBayesianPriorInputV2(ModelNormal):
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
        self_,
        arm_standard_deviation: Union[float, UnsetType] = unset,
        grand_mean: Union[float, UnsetType] = unset,
        grand_mean_standard_deviation: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        The prior the bandit's estimates start from, in the metric's units. Omitted fields keep their current values, or their defaults on create. A change takes effect on the next refresh.

        :param arm_standard_deviation: Prior standard deviation of each arm's mean around the shared mean. Must be between 1e-12 and 1e12. Defaults to 100.
        :type arm_standard_deviation: float, optional

        :param grand_mean: Prior mean of the shared mean of the arms. Its absolute value must be at most 1e12 times ``grand_mean_standard_deviation``. Defaults to 0.
        :type grand_mean: float, optional

        :param grand_mean_standard_deviation: Prior standard deviation of the shared mean of the arms. Must be between 1e-12 and 1e12, and at most 1e7 times ``arm_standard_deviation``. Defaults to 10000.
        :type grand_mean_standard_deviation: float, optional
        """
        if arm_standard_deviation is not unset:
            kwargs["arm_standard_deviation"] = arm_standard_deviation
        if grand_mean is not unset:
            kwargs["grand_mean"] = grand_mean
        if grand_mean_standard_deviation is not unset:
            kwargs["grand_mean_standard_deviation"] = grand_mean_standard_deviation
        super().__init__(kwargs)
