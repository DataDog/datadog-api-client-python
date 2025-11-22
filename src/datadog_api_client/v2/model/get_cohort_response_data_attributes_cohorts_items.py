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
    from datadog_api_client.v2.model.get_cohort_response_data_attributes_cohorts_items_values_items import (
        GetCohortResponseDataAttributesCohortsItemsValuesItems,
    )


class GetCohortResponseDataAttributesCohortsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.get_cohort_response_data_attributes_cohorts_items_values_items import (
            GetCohortResponseDataAttributesCohortsItemsValuesItems,
        )

        return {
            "cohort": (str,),
            "cohort_size": (int,),
            "start_time": (int,),
            "values": ([GetCohortResponseDataAttributesCohortsItemsValuesItems],),
        }

    attribute_map = {
        "cohort": "cohort",
        "cohort_size": "cohort_size",
        "start_time": "start_time",
        "values": "values",
    }

    def __init__(
        self_,
        cohort: Union[str, UnsetType] = unset,
        cohort_size: Union[int, UnsetType] = unset,
        start_time: Union[int, UnsetType] = unset,
        values: Union[List[GetCohortResponseDataAttributesCohortsItemsValuesItems], UnsetType] = unset,
        **kwargs,
    ):
        """


        :param cohort:
        :type cohort: str, optional

        :param cohort_size:
        :type cohort_size: int, optional

        :param start_time:
        :type start_time: int, optional

        :param values:
        :type values: [GetCohortResponseDataAttributesCohortsItemsValuesItems], optional
        """
        if cohort is not unset:
            kwargs["cohort"] = cohort
        if cohort_size is not unset:
            kwargs["cohort_size"] = cohort_size
        if start_time is not unset:
            kwargs["start_time"] = start_time
        if values is not unset:
            kwargs["values"] = values
        super().__init__(kwargs)
