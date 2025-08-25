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
    from datadog_api_client.v2.model.component_recommendation import ComponentRecommendation


class RecommendationAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.component_recommendation import ComponentRecommendation

        return {
            "driver": (ComponentRecommendation,),
            "executor": (ComponentRecommendation,),
        }

    attribute_map = {
        "driver": "driver",
        "executor": "executor",
    }

    def __init__(self_, driver: ComponentRecommendation, executor: ComponentRecommendation, **kwargs):
        """
        Attributes of the SPA Recommendation resource. Contains recommendations for both driver and executor components.

        :param driver: Resource recommendation for a single Spark component (driver or executor). Contains estimation data used to patch Spark job specs.
        :type driver: ComponentRecommendation

        :param executor: Resource recommendation for a single Spark component (driver or executor). Contains estimation data used to patch Spark job specs.
        :type executor: ComponentRecommendation
        """
        super().__init__(kwargs)

        self_.driver = driver
        self_.executor = executor
