# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.dem_journey_rum import DemJourneyRum
    from datadog_api_client.v2.model.dem_test_suite_nested import DemTestSuiteNested
    from datadog_api_client.v2.model.dem_variant import DemVariant


class DemInferredJourneyIgnoredAttributes(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dem_journey_rum import DemJourneyRum
        from datadog_api_client.v2.model.dem_test_suite_nested import DemTestSuiteNested
        from datadog_api_client.v2.model.dem_variant import DemVariant

        return {
            "created_at": (datetime,),
            "description": (str, none_type),
            "ignored_at": (datetime,),
            "journey_rum": (DemJourneyRum,),
            "name": (str,),
            "org_id": (int,),
            "tags": ([str],),
            "test_suite": (DemTestSuiteNested,),
            "variants": ([DemVariant],),
        }

    attribute_map = {
        "created_at": "created_at",
        "description": "description",
        "ignored_at": "ignored_at",
        "journey_rum": "journey_rum",
        "name": "name",
        "org_id": "org_id",
        "tags": "tags",
        "test_suite": "test_suite",
        "variants": "variants",
    }
    read_only_vars = {
        "created_at",
        "ignored_at",
        "org_id",
    }

    def __init__(
        self_,
        created_at: datetime,
        ignored_at: datetime,
        journey_rum: DemJourneyRum,
        name: str,
        org_id: int,
        tags: List[str],
        variants: List[DemVariant],
        description: Union[str, none_type, UnsetType] = unset,
        test_suite: Union[DemTestSuiteNested, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an ignored inferred journey.

        :param created_at: Timestamp when the inferred journey was first observed.
        :type created_at: datetime

        :param description: An optional description of the inferred journey.
        :type description: str, none_type, optional

        :param ignored_at: Timestamp when the inferred journey was ignored.
        :type ignored_at: datetime

        :param journey_rum: The RUM definition for a DEM journey.
        :type journey_rum: DemJourneyRum

        :param name: The name of the inferred journey.
        :type name: str

        :param org_id: The organization ID that owns this inferred journey.
        :type org_id: int

        :param tags: List of tags associated with a DEM resource.
        :type tags: [str]

        :param test_suite: A test suite associated with a DEM resource.
        :type test_suite: DemTestSuiteNested, optional

        :param variants: List of variants associated with a DEM journey.
        :type variants: [DemVariant]
        """
        if description is not unset:
            kwargs["description"] = description
        if test_suite is not unset:
            kwargs["test_suite"] = test_suite
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.ignored_at = ignored_at
        self_.journey_rum = journey_rum
        self_.name = name
        self_.org_id = org_id
        self_.tags = tags
        self_.variants = variants
