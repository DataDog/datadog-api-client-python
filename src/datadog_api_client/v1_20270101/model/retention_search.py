# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.retention_search_cohort_criteria import RetentionSearchCohortCriteria
    from datadog_api_client.v1_20270101.model.retention_search_filters import RetentionSearchFilters
    from datadog_api_client.v1_20270101.model.retention_search_retention_entity import RetentionSearchRetentionEntity
    from datadog_api_client.v1_20270101.model.retention_search_return_condition import RetentionSearchReturnCondition
    from datadog_api_client.v1_20270101.model.retention_search_return_criteria import RetentionSearchReturnCriteria


class RetentionSearch(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.retention_search_cohort_criteria import RetentionSearchCohortCriteria
        from datadog_api_client.v1_20270101.model.retention_search_filters import RetentionSearchFilters
        from datadog_api_client.v1_20270101.model.retention_search_retention_entity import (
            RetentionSearchRetentionEntity,
        )
        from datadog_api_client.v1_20270101.model.retention_search_return_condition import (
            RetentionSearchReturnCondition,
        )
        from datadog_api_client.v1_20270101.model.retention_search_return_criteria import RetentionSearchReturnCriteria

        return {
            "cohort_criteria": (RetentionSearchCohortCriteria,),
            "filters": (RetentionSearchFilters,),
            "retention_entity": (RetentionSearchRetentionEntity,),
            "return_condition": (RetentionSearchReturnCondition,),
            "return_criteria": (RetentionSearchReturnCriteria,),
        }

    attribute_map = {
        "cohort_criteria": "cohort_criteria",
        "filters": "filters",
        "retention_entity": "retention_entity",
        "return_condition": "return_condition",
        "return_criteria": "return_criteria",
    }

    def __init__(
        self_,
        cohort_criteria: RetentionSearchCohortCriteria,
        retention_entity: RetentionSearchRetentionEntity,
        return_condition: RetentionSearchReturnCondition,
        filters: Union[RetentionSearchFilters, UnsetType] = unset,
        return_criteria: Union[RetentionSearchReturnCriteria, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param cohort_criteria: Test-only generated schema for the dashboard versioning proof of concept.
        :type cohort_criteria: RetentionSearchCohortCriteria

        :param filters: Test-only generated schema for the dashboard versioning proof of concept.
        :type filters: RetentionSearchFilters, optional

        :param retention_entity: Test-only generated schema for the dashboard versioning proof of concept.
        :type retention_entity: RetentionSearchRetentionEntity

        :param return_condition: Test-only generated schema for the dashboard versioning proof of concept.
        :type return_condition: RetentionSearchReturnCondition

        :param return_criteria: Test-only generated schema for the dashboard versioning proof of concept.
        :type return_criteria: RetentionSearchReturnCriteria, optional
        """
        if filters is not unset:
            kwargs["filters"] = filters
        if return_criteria is not unset:
            kwargs["return_criteria"] = return_criteria
        super().__init__(kwargs)

        self_.cohort_criteria = cohort_criteria
        self_.retention_entity = retention_entity
        self_.return_condition = return_condition
