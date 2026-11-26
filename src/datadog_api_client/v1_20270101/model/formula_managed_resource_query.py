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
    from datadog_api_client.v1_20270101.model.dataset_compute import DatasetCompute
    from datadog_api_client.v1_20270101.model.formula_managed_resource_query_data_source import (
        FormulaManagedResourceQueryDataSource,
    )
    from datadog_api_client.v1_20270101.model.dataset_group_by import DatasetGroupBy


class FormulaManagedResourceQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.dataset_compute import DatasetCompute
        from datadog_api_client.v1_20270101.model.formula_managed_resource_query_data_source import (
            FormulaManagedResourceQueryDataSource,
        )
        from datadog_api_client.v1_20270101.model.dataset_group_by import DatasetGroupBy

        return {
            "compute": ([DatasetCompute],),
            "data_source": (FormulaManagedResourceQueryDataSource,),
            "group_by": ([DatasetGroupBy],),
            "name": (str,),
            "query_filter": (str,),
            "table_name": (str,),
        }

    attribute_map = {
        "compute": "compute",
        "data_source": "data_source",
        "group_by": "group_by",
        "name": "name",
        "query_filter": "query_filter",
        "table_name": "table_name",
    }

    def __init__(
        self_,
        compute: List[DatasetCompute],
        data_source: FormulaManagedResourceQueryDataSource,
        name: str,
        table_name: str,
        group_by: Union[List[DatasetGroupBy], UnsetType] = unset,
        query_filter: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param compute: Test-only generated schema for the dashboard versioning proof of concept.
        :type compute: [DatasetCompute]

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: FormulaManagedResourceQueryDataSource

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: [DatasetGroupBy], optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param query_filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type query_filter: str, optional

        :param table_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type table_name: str
        """
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if query_filter is not unset:
            kwargs["query_filter"] = query_filter
        super().__init__(kwargs)

        self_.compute = compute
        self_.data_source = data_source
        self_.name = name
        self_.table_name = table_name
