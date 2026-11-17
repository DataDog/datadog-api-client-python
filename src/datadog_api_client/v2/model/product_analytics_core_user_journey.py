# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ProductAnalyticsCoreUserJourney(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "expression": (str,),
            "score": (int,),
            "steps": ({str: (str,)},),
            "support": (int,),
        }

    attribute_map = {
        "expression": "expression",
        "score": "score",
        "steps": "steps",
        "support": "support",
    }

    def __init__(
        self_,
        expression: Union[str, UnsetType] = unset,
        score: Union[int, UnsetType] = unset,
        steps: Union[Dict[str, str], UnsetType] = unset,
        support: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        A sequence of events that users follow to use a feature.

        :param expression: Order of the steps, as step IDs joined by ``->``.
        :type expression: str, optional

        :param score: Relevance score of the journey. Higher is more relevant.
        :type score: int, optional

        :param steps: Map of step ID to the event query of the step.
        :type steps: {str: (str,)}, optional

        :param support: Number of sessions that followed the journey.
        :type support: int, optional
        """
        if expression is not unset:
            kwargs["expression"] = expression
        if score is not unset:
            kwargs["score"] = score
        if steps is not unset:
            kwargs["steps"] = steps
        if support is not unset:
            kwargs["support"] = support
        super().__init__(kwargs)
