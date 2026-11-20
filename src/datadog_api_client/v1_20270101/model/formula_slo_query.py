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
    from datadog_api_client.v1_20270101.model.formula_slo_query_data_source import FormulaSloQueryDataSource
    from datadog_api_client.v1_20270101.model.slo_group_mode import SloGroupMode
    from datadog_api_client.v1_20270101.model.slo_measure import SloMeasure
    from datadog_api_client.v1_20270101.model.slo_query_type import SloQueryType
    from datadog_api_client.v1_20270101.model.slo_time_window import SloTimeWindow


class FormulaSloQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.formula_slo_query_data_source import FormulaSloQueryDataSource
        from datadog_api_client.v1_20270101.model.slo_group_mode import SloGroupMode
        from datadog_api_client.v1_20270101.model.slo_measure import SloMeasure
        from datadog_api_client.v1_20270101.model.slo_query_type import SloQueryType
        from datadog_api_client.v1_20270101.model.slo_time_window import SloTimeWindow

        return {
            "additional_query_filters": (str,),
            "apply_corrections": (bool,),
            "data_source": (FormulaSloQueryDataSource,),
            "group_mode": (SloGroupMode,),
            "measure": (SloMeasure,),
            "name": (str,),
            "slo_id": (str,),
            "slo_query_type": (SloQueryType,),
            "slo_time_window": (SloTimeWindow,),
        }

    attribute_map = {
        "additional_query_filters": "additional_query_filters",
        "apply_corrections": "apply_corrections",
        "data_source": "data_source",
        "group_mode": "group_mode",
        "measure": "measure",
        "name": "name",
        "slo_id": "slo_id",
        "slo_query_type": "slo_query_type",
        "slo_time_window": "slo_time_window",
    }

    def __init__(
        self_,
        data_source: FormulaSloQueryDataSource,
        group_mode: SloGroupMode,
        measure: Union[SloMeasure, str],
        name: str,
        slo_id: str,
        slo_query_type: SloQueryType,
        additional_query_filters: Union[str, UnsetType] = unset,
        apply_corrections: Union[bool, UnsetType] = unset,
        slo_time_window: Union[SloTimeWindow, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param additional_query_filters: Test-only generated schema for the dashboard versioning proof of concept.
        :type additional_query_filters: str, optional

        :param apply_corrections: Test-only generated schema for the dashboard versioning proof of concept.
        :type apply_corrections: bool, optional

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: FormulaSloQueryDataSource

        :param group_mode: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_mode: SloGroupMode

        :param measure: Test-only generated schema for the dashboard versioning proof of concept.
        :type measure: SloMeasure

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param slo_id: Test-only generated schema for the dashboard versioning proof of concept.
        :type slo_id: str

        :param slo_query_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type slo_query_type: SloQueryType

        :param slo_time_window: Test-only generated schema for the dashboard versioning proof of concept.
        :type slo_time_window: SloTimeWindow, optional
        """
        if additional_query_filters is not unset:
            kwargs["additional_query_filters"] = additional_query_filters
        if apply_corrections is not unset:
            kwargs["apply_corrections"] = apply_corrections
        if slo_time_window is not unset:
            kwargs["slo_time_window"] = slo_time_window
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.group_mode = group_mode
        self_.measure = measure
        self_.name = name
        self_.slo_id = slo_id
        self_.slo_query_type = slo_query_type
