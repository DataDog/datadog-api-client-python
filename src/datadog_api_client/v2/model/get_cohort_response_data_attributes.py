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
    from datadog_api_client.v2.model.get_cohort_response_data_attributes_cohorts_items import (
        GetCohortResponseDataAttributesCohortsItems,
    )


class GetCohortResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.get_cohort_response_data_attributes_cohorts_items import (
            GetCohortResponseDataAttributesCohortsItems,
        )

        return {
            "cohorts": ([GetCohortResponseDataAttributesCohortsItems],),
        }

    attribute_map = {
        "cohorts": "cohorts",
    }

    def __init__(self_, cohorts: Union[List[GetCohortResponseDataAttributesCohortsItems], UnsetType] = unset, **kwargs):
        """


        :param cohorts:
        :type cohorts: [GetCohortResponseDataAttributesCohortsItems], optional
        """
        if cohorts is not unset:
            kwargs["cohorts"] = cohorts
        super().__init__(kwargs)
