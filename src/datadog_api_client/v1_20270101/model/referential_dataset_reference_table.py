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
    from datadog_api_client.v1_20270101.model.referential_dataset_reference_table_data_source import (
        ReferentialDatasetReferenceTableDataSource,
    )


class ReferentialDatasetReferenceTable(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.referential_dataset_reference_table_data_source import (
            ReferentialDatasetReferenceTableDataSource,
        )

        return {
            "data_source": (ReferentialDatasetReferenceTableDataSource,),
            "name": (str,),
            "query_filter": (str,),
            "table_name": (str,),
        }

    attribute_map = {
        "data_source": "data_source",
        "name": "name",
        "query_filter": "query_filter",
        "table_name": "table_name",
    }

    def __init__(
        self_,
        data_source: ReferentialDatasetReferenceTableDataSource,
        name: str,
        table_name: str,
        query_filter: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: ReferentialDatasetReferenceTableDataSource

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param query_filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type query_filter: str, optional

        :param table_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type table_name: str
        """
        if query_filter is not unset:
            kwargs["query_filter"] = query_filter
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.name = name
        self_.table_name = table_name
