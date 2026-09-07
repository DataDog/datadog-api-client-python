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
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.dem_user import DemUser
    from datadog_api_client.v2.model.dem_journey_rum import DemJourneyRum
    from datadog_api_client.v2.model.dem_test_suite_nested import DemTestSuiteNested
    from datadog_api_client.v2.model.dem_variant import DemVariant


class DemJourneyResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dem_user import DemUser
        from datadog_api_client.v2.model.dem_journey_rum import DemJourneyRum
        from datadog_api_client.v2.model.dem_test_suite_nested import DemTestSuiteNested
        from datadog_api_client.v2.model.dem_variant import DemVariant

        return {
            "created_at": (datetime,),
            "created_by": (DemUser,),
            "description": (str, none_type),
            "journey_rum": (DemJourneyRum,),
            "name": (str,),
            "org_id": (int,),
            "tags": ([str],),
            "test_suite": (DemTestSuiteNested,),
            "updated_at": (datetime, none_type),
            "updated_by": (DemUser,),
            "variants": ([DemVariant],),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "description": "description",
        "journey_rum": "journey_rum",
        "name": "name",
        "org_id": "org_id",
        "tags": "tags",
        "test_suite": "test_suite",
        "updated_at": "updated_at",
        "updated_by": "updated_by",
        "variants": "variants",
    }
    read_only_vars = {
        "created_at",
        "org_id",
        "updated_at",
    }

    def __init__(
        self_,
        created_at: datetime,
        created_by: DemUser,
        description: Union[str, none_type],
        journey_rum: DemJourneyRum,
        name: str,
        org_id: int,
        tags: List[str],
        test_suite: DemTestSuiteNested,
        updated_at: Union[datetime, none_type],
        updated_by: DemUser,
        variants: List[DemVariant],
        **kwargs,
    ):
        """
        Attributes returned in a DEM journey response.

        :param created_at: The timestamp when the journey was created.
        :type created_at: datetime

        :param created_by: A Datadog user associated with a DEM operation.
        :type created_by: DemUser

        :param description: An optional human-readable description of the journey.
        :type description: str, none_type

        :param journey_rum: The RUM definition for a DEM journey.
        :type journey_rum: DemJourneyRum

        :param name: The name of the DEM journey.
        :type name: str

        :param org_id: The organization ID that owns this journey.
        :type org_id: int

        :param tags: List of tags associated with a DEM resource.
        :type tags: [str]

        :param test_suite: A test suite associated with a DEM resource.
        :type test_suite: DemTestSuiteNested

        :param updated_at: The timestamp when the journey was last updated.
        :type updated_at: datetime, none_type

        :param updated_by: A Datadog user associated with a DEM operation.
        :type updated_by: DemUser

        :param variants: List of variants associated with a DEM journey.
        :type variants: [DemVariant]
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.created_by = created_by
        self_.description = description
        self_.journey_rum = journey_rum
        self_.name = name
        self_.org_id = org_id
        self_.tags = tags
        self_.test_suite = test_suite
        self_.updated_at = updated_at
        self_.updated_by = updated_by
        self_.variants = variants
