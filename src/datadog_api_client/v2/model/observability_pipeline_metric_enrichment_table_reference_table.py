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
    from datadog_api_client.v2.model.observability_pipeline_metric_enrichment_table_reference_key import (
        ObservabilityPipelineMetricEnrichmentTableReferenceKey,
    )


class ObservabilityPipelineMetricEnrichmentTableReferenceTable(ModelNormal):
    validations = {
        "columns": {
            "max_items": 50,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_metric_enrichment_table_reference_key import (
            ObservabilityPipelineMetricEnrichmentTableReferenceKey,
        )

        return {
            "app_key_key": (str,),
            "columns": ([str],),
            "key": (ObservabilityPipelineMetricEnrichmentTableReferenceKey,),
            "table_id": (str,),
        }

    attribute_map = {
        "app_key_key": "app_key_key",
        "columns": "columns",
        "key": "key",
        "table_id": "table_id",
    }

    def __init__(
        self_,
        key: ObservabilityPipelineMetricEnrichmentTableReferenceKey,
        table_id: str,
        app_key_key: Union[str, UnsetType] = unset,
        columns: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Uses a Datadog reference table to enrich metrics.

        :param app_key_key: The name of the environment variable or secret that holds the Datadog application key used to access the
            reference table.
        :type app_key_key: str, optional

        :param columns: A list of column names to include from the reference table. If not provided, all columns are included.
        :type columns: [str], optional

        :param key: Defines the metric lookup value used as the reference-table row ID.
        :type key: ObservabilityPipelineMetricEnrichmentTableReferenceKey

        :param table_id: The unique identifier of the reference table.
        :type table_id: str
        """
        if app_key_key is not unset:
            kwargs["app_key_key"] = app_key_key
        if columns is not unset:
            kwargs["columns"] = columns
        super().__init__(kwargs)

        self_.key = key
        self_.table_id = table_id
