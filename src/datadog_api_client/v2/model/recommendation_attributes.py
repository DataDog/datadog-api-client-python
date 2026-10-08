# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.component_recommendation import ComponentRecommendation


class RecommendationAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.component_recommendation import ComponentRecommendation

        return {
            "confidence_level": (float,),
            "driver": (ComponentRecommendation,),
            "executor": (ComponentRecommendation,),
            "matched_params": (str,),
        }

    attribute_map = {
        "confidence_level": "confidence_level",
        "driver": "driver",
        "executor": "executor",
        "matched_params": "matched_params",
    }

    def __init__(
        self_,
        driver: ComponentRecommendation,
        executor: ComponentRecommendation,
        confidence_level: Union[float, UnsetType] = unset,
        matched_params: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the SPA Recommendation resource. Contains recommendations for both driver and executor components.

        :param confidence_level: The confidence level of the recommendation, expressed as a value between 0.0 (low confidence) and 1.0 (high confidence).
        :type confidence_level: float, optional

        :param driver: Resource recommendation for a single Spark component (driver or executor). Contains estimation data used to patch Spark job specs.
        :type driver: ComponentRecommendation

        :param executor: Resource recommendation for a single Spark component (driver or executor). Contains estimation data used to patch Spark job specs.
        :type executor: ComponentRecommendation

        :param matched_params: Only returned by the v2 endpoint. The job parameters whose values the recommendation was matched on, as ``parameter=value`` pairs joined by ``|``.
            An empty string means the service-wide (coarse) recommendation was used.
        :type matched_params: str, optional
        """
        if confidence_level is not unset:
            kwargs["confidence_level"] = confidence_level
        if matched_params is not unset:
            kwargs["matched_params"] = matched_params
        super().__init__(kwargs)

        self_.driver = driver
        self_.executor = executor
