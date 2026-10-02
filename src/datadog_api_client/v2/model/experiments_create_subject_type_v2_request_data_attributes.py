# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


class ExperimentsCreateSubjectTypeV2RequestDataAttributes(ModelNormal):
    validations = {
        "name": {
            "max_length": 40,
            "min_length": 3,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "migration_metadata": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
            "name": (str,),
            "product_analytics_attribute": (str,),
            "warehouse_column_names": ([str],),
        }

    attribute_map = {
        "migration_metadata": "migration_metadata",
        "name": "name",
        "product_analytics_attribute": "product_analytics_attribute",
        "warehouse_column_names": "warehouse_column_names",
    }

    def __init__(
        self_,
        name: str,
        migration_metadata: Union[Any, UnsetType] = unset,
        product_analytics_attribute: Union[str, UnsetType] = unset,
        warehouse_column_names: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Name and data field mappings for the new subject type.

        :param migration_metadata: Metadata associated with migration of this resource.
        :type migration_metadata: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param name: Display name of the subject type.
        :type name: str

        :param product_analytics_attribute: Product Analytics attribute used to identify subjects of this type.
        :type product_analytics_attribute: str, optional

        :param warehouse_column_names: Warehouse column names associated with this subject type.
        :type warehouse_column_names: [str], optional
        """
        if migration_metadata is not unset:
            kwargs["migration_metadata"] = migration_metadata
        if product_analytics_attribute is not unset:
            kwargs["product_analytics_attribute"] = product_analytics_attribute
        if warehouse_column_names is not unset:
            kwargs["warehouse_column_names"] = warehouse_column_names
        super().__init__(kwargs)

        self_.name = name
