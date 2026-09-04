# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.dem_rum_step import DemRumStep


class DemVariantAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dem_rum_step import DemRumStep

        return {
            "filter": (str,),
            "name": (str,),
            "rum_steps": ([DemRumStep],),
        }

    attribute_map = {
        "filter": "filter",
        "name": "name",
        "rum_steps": "rum_steps",
    }

    def __init__(self_, name: str, rum_steps: List[DemRumStep], filter: Union[str, UnsetType] = unset, **kwargs):
        """
        Attributes of a DEM journey variant.

        :param filter: An optional RUM query filter to scope this variant.
        :type filter: str, optional

        :param name: The name of the variant.
        :type name: str

        :param rum_steps: List of RUM journey steps.
        :type rum_steps: [DemRumStep]
        """
        if filter is not unset:
            kwargs["filter"] = filter
        super().__init__(kwargs)

        self_.name = name
        self_.rum_steps = rum_steps
