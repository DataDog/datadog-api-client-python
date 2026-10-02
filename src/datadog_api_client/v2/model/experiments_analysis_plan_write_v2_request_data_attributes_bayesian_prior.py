# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class ExperimentsAnalysisPlanWriteV2RequestDataAttributesBayesianPrior(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "degrees_of_freedom": (float, none_type),
            "standard_deviation": (float,),
        }

    attribute_map = {
        "degrees_of_freedom": "degrees_of_freedom",
        "standard_deviation": "standard_deviation",
    }

    def __init__(
        self_, standard_deviation: float, degrees_of_freedom: Union[float, none_type, UnsetType] = unset, **kwargs
    ):
        """
        Parameters of the prior distribution to use for Bayesian analysis.

        :param degrees_of_freedom: Degrees of freedom of the prior distribution.
        :type degrees_of_freedom: float, none_type, optional

        :param standard_deviation: Standard deviation of the prior distribution.
        :type standard_deviation: float
        """
        if degrees_of_freedom is not unset:
            kwargs["degrees_of_freedom"] = degrees_of_freedom
        super().__init__(kwargs)

        self_.standard_deviation = standard_deviation
