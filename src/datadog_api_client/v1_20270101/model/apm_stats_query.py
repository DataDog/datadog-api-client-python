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
    from datadog_api_client.v1_20270101.model.query_table_column_request import QueryTableColumnRequest
    from datadog_api_client.v1_20270101.model.apm_stats_query_row_type import ApmStatsQueryRowType


class ApmStatsQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.query_table_column_request import QueryTableColumnRequest
        from datadog_api_client.v1_20270101.model.apm_stats_query_row_type import ApmStatsQueryRowType

        return {
            "columns": ([QueryTableColumnRequest],),
            "env": (str,),
            "name": (str,),
            "primary_tag": (str,),
            "resource": (str,),
            "row_type": (ApmStatsQueryRowType,),
            "service": (str,),
        }

    attribute_map = {
        "columns": "columns",
        "env": "env",
        "name": "name",
        "primary_tag": "primary_tag",
        "resource": "resource",
        "row_type": "row_type",
        "service": "service",
    }

    def __init__(
        self_,
        env: str,
        name: str,
        primary_tag: str,
        row_type: ApmStatsQueryRowType,
        service: str,
        columns: Union[List[QueryTableColumnRequest], UnsetType] = unset,
        resource: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type columns: [QueryTableColumnRequest], optional

        :param env: Test-only generated schema for the dashboard versioning proof of concept.
        :type env: str

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param primary_tag: Test-only generated schema for the dashboard versioning proof of concept.
        :type primary_tag: str

        :param resource: Test-only generated schema for the dashboard versioning proof of concept.
        :type resource: str, optional

        :param row_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type row_type: ApmStatsQueryRowType

        :param service: Test-only generated schema for the dashboard versioning proof of concept.
        :type service: str
        """
        if columns is not unset:
            kwargs["columns"] = columns
        if resource is not unset:
            kwargs["resource"] = resource
        super().__init__(kwargs)

        self_.env = env
        self_.name = name
        self_.primary_tag = primary_tag
        self_.row_type = row_type
        self_.service = service
