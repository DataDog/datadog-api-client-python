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


class ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsConfidenceInterval(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "lower": (float,),
            "upper": (float,),
        }

    attribute_map = {
        "lower": "lower",
        "upper": "upper",
    }

    def __init__(self_, lower: Union[float, UnsetType] = unset, upper: Union[float, UnsetType] = unset, **kwargs):
        """
        Lower and upper bounds of the reported statistical interval.

        :param lower: Lower bound of the reported interval.
        :type lower: float, optional

        :param upper: Upper bound of the reported interval.
        :type upper: float, optional
        """
        if lower is not unset:
            kwargs["lower"] = lower
        if upper is not unset:
            kwargs["upper"] = upper
        super().__init__(kwargs)
