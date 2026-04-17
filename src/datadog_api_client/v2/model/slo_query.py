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
    from datadog_api_client.v2.model.slo_data_source import SloDataSource
    from datadog_api_client.v2.model.slos_group_mode import SlosGroupMode
    from datadog_api_client.v2.model.slos_measure import SlosMeasure
    from datadog_api_client.v2.model.slos_query_type import SlosQueryType


class SloQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.slo_data_source import SloDataSource
        from datadog_api_client.v2.model.slos_group_mode import SlosGroupMode
        from datadog_api_client.v2.model.slos_measure import SlosMeasure
        from datadog_api_client.v2.model.slos_query_type import SlosQueryType

        return {
            "additional_query_filters": (str,),
            "data_source": (SloDataSource,),
            "group_mode": (SlosGroupMode,),
            "measure": (SlosMeasure,),
            "name": (str,),
            "slo_id": (str,),
            "slo_query_type": (SlosQueryType,),
        }

    attribute_map = {
        "additional_query_filters": "additional_query_filters",
        "data_source": "data_source",
        "group_mode": "group_mode",
        "measure": "measure",
        "name": "name",
        "slo_id": "slo_id",
        "slo_query_type": "slo_query_type",
    }

    def __init__(
        self_,
        data_source: SloDataSource,
        measure: SlosMeasure,
        slo_id: str,
        additional_query_filters: Union[str, UnsetType] = unset,
        group_mode: Union[SlosGroupMode, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        slo_query_type: Union[SlosQueryType, UnsetType] = unset,
        **kwargs,
    ):
        """
        A query for SLO status, error budget, and burn rate metrics.

        :param additional_query_filters: Additional filters applied to the SLO query.
        :type additional_query_filters: str, optional

        :param data_source: A data source for SLO queries.
        :type data_source: SloDataSource

        :param group_mode: How SLO results are grouped in the response.
        :type group_mode: SlosGroupMode, optional

        :param measure: The SLO measurement to retrieve.
        :type measure: SlosMeasure

        :param name: The variable name for use in formulas.
        :type name: str, optional

        :param slo_id: The unique identifier of the SLO to query.
        :type slo_id: str

        :param slo_query_type: The type of SLO definition being queried.
        :type slo_query_type: SlosQueryType, optional
        """
        if additional_query_filters is not unset:
            kwargs["additional_query_filters"] = additional_query_filters
        if group_mode is not unset:
            kwargs["group_mode"] = group_mode
        if name is not unset:
            kwargs["name"] = name
        if slo_query_type is not unset:
            kwargs["slo_query_type"] = slo_query_type
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.measure = measure
        self_.slo_id = slo_id
