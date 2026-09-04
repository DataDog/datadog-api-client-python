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
    from datadog_api_client.v2.model.dem_variant import DemVariant


class DemJourneyRum(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dem_rum_step import DemRumStep
        from datadog_api_client.v2.model.dem_variant import DemVariant

        return {
            "filter": (str,),
            "rum_steps": ([DemRumStep],),
            "variants": ([DemVariant],),
        }

    attribute_map = {
        "filter": "filter",
        "rum_steps": "rum_steps",
        "variants": "variants",
    }

    def __init__(
        self_,
        rum_steps: List[DemRumStep],
        filter: Union[str, UnsetType] = unset,
        variants: Union[List[DemVariant], UnsetType] = unset,
        **kwargs,
    ):
        """
        The RUM definition for a DEM journey.

        :param filter: An optional RUM query filter applied to the entire journey.
        :type filter: str, optional

        :param rum_steps: List of RUM journey steps.
        :type rum_steps: [DemRumStep]

        :param variants: List of variants associated with a DEM journey.
        :type variants: [DemVariant], optional
        """
        if filter is not unset:
            kwargs["filter"] = filter
        if variants is not unset:
            kwargs["variants"] = variants
        super().__init__(kwargs)

        self_.rum_steps = rum_steps
