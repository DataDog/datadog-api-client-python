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
    from datadog_api_client.v2.model.dem_journey_rum import DemJourneyRum
    from datadog_api_client.v2.model.dem_variant import DemVariant


class DemJourneyCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dem_journey_rum import DemJourneyRum
        from datadog_api_client.v2.model.dem_variant import DemVariant

        return {
            "description": (str,),
            "journey_rum": (DemJourneyRum,),
            "name": (str,),
            "tags": ([str],),
            "variants": ([DemVariant],),
        }

    attribute_map = {
        "description": "description",
        "journey_rum": "journey_rum",
        "name": "name",
        "tags": "tags",
        "variants": "variants",
    }

    def __init__(
        self_,
        journey_rum: DemJourneyRum,
        name: str,
        tags: List[str],
        description: Union[str, UnsetType] = unset,
        variants: Union[List[DemVariant], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating or updating a DEM journey.

        :param description: An optional human-readable description of the journey.
        :type description: str, optional

        :param journey_rum: The RUM definition for a DEM journey.
        :type journey_rum: DemJourneyRum

        :param name: The name of the DEM journey.
        :type name: str

        :param tags: List of tags associated with a DEM resource.
        :type tags: [str]

        :param variants: List of variants associated with a DEM journey.
        :type variants: [DemVariant], optional
        """
        if description is not unset:
            kwargs["description"] = description
        if variants is not unset:
            kwargs["variants"] = variants
        super().__init__(kwargs)

        self_.journey_rum = journey_rum
        self_.name = name
        self_.tags = tags
