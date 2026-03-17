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


class ProductAnalyticsSankeyDefinition(ModelNormal):
    validations = {
        "entries_per_step": {
            "inclusive_maximum": 10,
        },
        "number_of_steps": {
            "inclusive_maximum": 10,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "entries_per_step": (int,),
            "number_of_steps": (int,),
            "source": (str,),
            "target": (str,),
        }

    attribute_map = {
        "entries_per_step": "entries_per_step",
        "number_of_steps": "number_of_steps",
        "source": "source",
        "target": "target",
    }

    def __init__(
        self_,
        entries_per_step: Union[int, UnsetType] = unset,
        number_of_steps: Union[int, UnsetType] = unset,
        source: Union[str, UnsetType] = unset,
        target: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Sankey visualization definition. Set either ``source`` or ``target`` , not both.
        Use ``source`` for forward flow (where do users go after this page?) or
        ``target`` for backward flow (where did users come from?).

        :param entries_per_step: Number of page entries per step. Default 5, max 10.
        :type entries_per_step: int, optional

        :param number_of_steps: Number of steps in the flow. Default 5, max 10.
        :type number_of_steps: int, optional

        :param source: The source page for forward flow analysis. Use "*" for all pages.
        :type source: str, optional

        :param target: The target page for backward flow analysis.
        :type target: str, optional
        """
        if entries_per_step is not unset:
            kwargs["entries_per_step"] = entries_per_step
        if number_of_steps is not unset:
            kwargs["number_of_steps"] = number_of_steps
        if source is not unset:
            kwargs["source"] = source
        if target is not unset:
            kwargs["target"] = target
        super().__init__(kwargs)
