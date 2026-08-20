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
            "inclusive_minimum": 0,
        },
        "number_of_steps": {
            "inclusive_maximum": 10,
            "inclusive_minimum": 0,
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
        source: str,
        target: str,
        entries_per_step: Union[int, UnsetType] = unset,
        number_of_steps: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        The shape of the Sankey diagram, expressed as the facets to flow between and how many steps to show.

        :param entries_per_step: Maximum number of nodes to keep in each column. Remaining values are rolled up into an
            aggregated node. Omit it, or send ``0`` , to use the default of ``5``.
        :type entries_per_step: int, optional

        :param number_of_steps: Number of intermediate columns between the source and the target.
            Omit it, or send ``0`` , to use the default of ``5``.
        :type number_of_steps: int, optional

        :param source: Facet forming the first column of the diagram.
        :type source: str

        :param target: Facet forming the last column of the diagram.
        :type target: str
        """
        if entries_per_step is not unset:
            kwargs["entries_per_step"] = entries_per_step
        if number_of_steps is not unset:
            kwargs["number_of_steps"] = number_of_steps
        super().__init__(kwargs)

        self_.source = source
        self_.target = target
