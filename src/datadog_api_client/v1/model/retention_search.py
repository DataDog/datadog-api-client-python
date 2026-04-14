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
    from datadog_api_client.v1.model.retention_cohort_criteria import RetentionCohortCriteria
    from datadog_api_client.v1.model.retention_filters import RetentionFilters
    from datadog_api_client.v1.model.retention_entity import RetentionEntity
    from datadog_api_client.v1.model.retention_return_condition import RetentionReturnCondition
    from datadog_api_client.v1.model.retention_return_criteria import RetentionReturnCriteria


class RetentionSearch(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.retention_cohort_criteria import RetentionCohortCriteria
        from datadog_api_client.v1.model.retention_filters import RetentionFilters
        from datadog_api_client.v1.model.retention_entity import RetentionEntity
        from datadog_api_client.v1.model.retention_return_condition import RetentionReturnCondition
        from datadog_api_client.v1.model.retention_return_criteria import RetentionReturnCriteria

        return {
            "cohort_criteria": (RetentionCohortCriteria,),
            "filters": (RetentionFilters,),
            "retention_entity": (RetentionEntity,),
            "return_condition": (RetentionReturnCondition,),
            "return_criteria": (RetentionReturnCriteria,),
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
        cohort_criteria: RetentionCohortCriteria,
        retention_entity: RetentionEntity,
        return_condition: RetentionReturnCondition,
        filters: Union[RetentionFilters, UnsetType] = unset,
        return_criteria: Union[RetentionReturnCriteria, UnsetType] = unset,
        **kwargs,
    ):
        """
        Search configuration for retention queries.

        :param cohort_criteria: Cohort criteria for retention queries.
        :type cohort_criteria: RetentionCohortCriteria

        :param filters: Filters for retention queries.
        :type filters: RetentionFilters, optional

        :param retention_entity: Entity to track for retention.
        :type retention_entity: RetentionEntity

        :param return_condition: Condition for counting user return.
        :type return_condition: RetentionReturnCondition

        :param return_criteria: Return criteria for retention queries.
        :type return_criteria: RetentionReturnCriteria, optional
        """
        if filters is not unset:
            kwargs["filters"] = filters
        if return_criteria is not unset:
            kwargs["return_criteria"] = return_criteria
        super().__init__(kwargs)

        self_.cohort_criteria = cohort_criteria
        self_.retention_entity = retention_entity
        self_.return_condition = return_condition
