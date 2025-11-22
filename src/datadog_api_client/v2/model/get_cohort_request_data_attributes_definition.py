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
    from datadog_api_client.v2.model.get_cohort_request_data_attributes_definition_audience_filters import (
        GetCohortRequestDataAttributesDefinitionAudienceFilters,
    )


class GetCohortRequestDataAttributesDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.get_cohort_request_data_attributes_definition_audience_filters import (
            GetCohortRequestDataAttributesDefinitionAudienceFilters,
        )

        return {
            "audience_filters": (GetCohortRequestDataAttributesDefinitionAudienceFilters,),
            "inclusion_search": (str,),
            "return_search": (str,),
            "segment_id": (str,),
        }

    attribute_map = {
        "audience_filters": "audience_filters",
        "inclusion_search": "inclusion_search",
        "return_search": "return_search",
        "segment_id": "segment_id",
    }

    def __init__(
        self_,
        audience_filters: Union[GetCohortRequestDataAttributesDefinitionAudienceFilters, UnsetType] = unset,
        inclusion_search: Union[str, UnsetType] = unset,
        return_search: Union[str, UnsetType] = unset,
        segment_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param audience_filters:
        :type audience_filters: GetCohortRequestDataAttributesDefinitionAudienceFilters, optional

        :param inclusion_search:
        :type inclusion_search: str, optional

        :param return_search:
        :type return_search: str, optional

        :param segment_id:
        :type segment_id: str, optional
        """
        if audience_filters is not unset:
            kwargs["audience_filters"] = audience_filters
        if inclusion_search is not unset:
            kwargs["inclusion_search"] = inclusion_search
        if return_search is not unset:
            kwargs["return_search"] = return_search
        if segment_id is not unset:
            kwargs["segment_id"] = segment_id
        super().__init__(kwargs)
