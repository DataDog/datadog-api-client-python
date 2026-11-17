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


class ProductAnalyticsFunnelStepSuggestionsRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "application_id": (str,),
            "expression": (str,),
            "steps": ({str: (str,)},),
        }

    attribute_map = {
        "application_id": "application_id",
        "expression": "expression",
        "steps": "steps",
    }

    def __init__(
        self_, expression: str, steps: Dict[str, str], application_id: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Attributes of a step suggestions request.

        :param application_id: Only use journeys from this RUM application.
        :type application_id: str, optional

        :param expression: Order of the funnel steps, as step IDs joined by ``->``.
        :type expression: str

        :param steps: Map of step ID to the event query of the step. Steps are matched in the string sort
            order of their IDs, so use zero-padded IDs such as ``node_01`` and ``node_02``. Without padding,
            ``node_10`` sorts before ``node_2``.
        :type steps: {str: (str,)}
        """
        if application_id is not unset:
            kwargs["application_id"] = application_id
        super().__init__(kwargs)

        self_.expression = expression
        self_.steps = steps
