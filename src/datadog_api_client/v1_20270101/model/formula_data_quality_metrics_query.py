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
    from datadog_api_client.v1_20270101.model.formula_data_quality_metrics_query_anomaly_options import (
        FormulaDataQualityMetricsQueryAnomalyOptions,
    )
    from datadog_api_client.v1_20270101.model.formula_data_quality_metrics_query_data_source import (
        FormulaDataQualityMetricsQueryDataSource,
    )


class FormulaDataQualityMetricsQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.formula_data_quality_metrics_query_anomaly_options import (
            FormulaDataQualityMetricsQueryAnomalyOptions,
        )
        from datadog_api_client.v1_20270101.model.formula_data_quality_metrics_query_data_source import (
            FormulaDataQualityMetricsQueryDataSource,
        )

        return {
            "anomaly_options": (FormulaDataQualityMetricsQueryAnomalyOptions,),
            "data_source": (FormulaDataQualityMetricsQueryDataSource,),
            "filter": (str,),
            "group_by": ([str],),
            "measure": (str,),
            "name": (str,),
            "scope": (str,),
        }

    attribute_map = {
        "anomaly_options": "anomaly_options",
        "data_source": "data_source",
        "filter": "filter",
        "group_by": "group_by",
        "measure": "measure",
        "name": "name",
        "scope": "scope",
    }

    def __init__(
        self_,
        data_source: FormulaDataQualityMetricsQueryDataSource,
        filter: str,
        measure: str,
        name: str,
        anomaly_options: Union[FormulaDataQualityMetricsQueryAnomalyOptions, UnsetType] = unset,
        group_by: Union[List[str], UnsetType] = unset,
        scope: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param anomaly_options: Test-only generated schema for the dashboard versioning proof of concept.
        :type anomaly_options: FormulaDataQualityMetricsQueryAnomalyOptions, optional

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: FormulaDataQualityMetricsQueryDataSource

        :param filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type filter: str

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: [str], optional

        :param measure: Test-only generated schema for the dashboard versioning proof of concept.
        :type measure: str

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param scope: Test-only generated schema for the dashboard versioning proof of concept.
        :type scope: str, optional
        """
        if anomaly_options is not unset:
            kwargs["anomaly_options"] = anomaly_options
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if scope is not unset:
            kwargs["scope"] = scope
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.filter = filter
        self_.measure = measure
        self_.name = name
