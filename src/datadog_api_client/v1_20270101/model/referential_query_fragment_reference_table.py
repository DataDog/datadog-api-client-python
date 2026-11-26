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
    from datadog_api_client.v1_20270101.model.referential_query_fragment_reference_table_data_source import (
        ReferentialQueryFragmentReferenceTableDataSource,
    )


class ReferentialQueryFragmentReferenceTable(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.referential_query_fragment_reference_table_data_source import (
            ReferentialQueryFragmentReferenceTableDataSource,
        )

        return {
            "alias": (str,),
            "data_source": (ReferentialQueryFragmentReferenceTableDataSource,),
            "filter": (str,),
            "name": (str,),
            "table_name": (str,),
        }

    attribute_map = {
        "alias": "alias",
        "data_source": "data_source",
        "filter": "filter",
        "name": "name",
        "table_name": "table_name",
    }

    def __init__(
        self_,
        data_source: ReferentialQueryFragmentReferenceTableDataSource,
        name: str,
        table_name: str,
        alias: Union[str, UnsetType] = unset,
        filter: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param alias: Test-only generated schema for the dashboard versioning proof of concept.
        :type alias: str, optional

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: ReferentialQueryFragmentReferenceTableDataSource

        :param filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type filter: str, optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param table_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type table_name: str
        """
        if alias is not unset:
            kwargs["alias"] = alias
        if filter is not unset:
            kwargs["filter"] = filter
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.name = name
        self_.table_name = table_name
