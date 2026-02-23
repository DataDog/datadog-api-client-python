# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ObservabilityPipelineEnrichmentTableReferenceTable(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "app_key_key": (str,),
            "columns": ([str],),
            "key_field": (str,),
            "table_id": (str,),
        }

    attribute_map = {
        "app_key_key": "app_key_key",
        "columns": "columns",
        "key_field": "key_field",
        "table_id": "table_id",
    }

    def __init__(
        self_,
        key_field: str,
        table_id: str,
        app_key_key: Union[str, UnsetType] = unset,
        columns: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Uses a Datadog reference table to enrich logs.

        :param app_key_key: Name of the environment variable or secret that holds the Datadog application key used to access the reference table.
        :type app_key_key: str, optional

        :param columns: List of column names to include from the reference table. If not provided, all columns are included.
        :type columns: [str], optional

        :param key_field: Path to the field in the log event to match against the reference table.
        :type key_field: str

        :param table_id: The unique identifier of the reference table.
        :type table_id: str
        """
        if app_key_key is not unset:
            kwargs["app_key_key"] = app_key_key
        if columns is not unset:
            kwargs["columns"] = columns
        super().__init__(kwargs)

        self_.key_field = key_field
        self_.table_id = table_id
