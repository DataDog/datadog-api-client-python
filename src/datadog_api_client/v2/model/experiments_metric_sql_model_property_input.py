# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Union, TYPE_CHECKING

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


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_create_exposure_sql_model_v2_request_data_attributes_items_column_type import (
        ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType,
    )


class ExperimentsMetricSQLModelPropertyInput(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_create_exposure_sql_model_v2_request_data_attributes_items_column_type import (
            ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType,
        )

        return {
            "column_name": (str,),
            "column_type": (ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType,),
            "description": (str, none_type),
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
        }

    attribute_map = {
        "column_name": "column_name",
        "column_type": "column_type",
        "description": "description",
        "migration_metadata": "migration_metadata",
        "name": "name",
    }

    def __init__(
        self_,
        column_name: str,
        column_type: ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType,
        name: str,
        description: Union[str, none_type, UnsetType] = unset,
        migration_metadata: Union[Any, UnsetType] = unset,
        **kwargs,
    ):
        """
        A property column defined by a metric SQL model.

        :param column_name: Name of the SQL result column that supplies this property.
        :type column_name: str

        :param column_type: Data type of a column in the SQL model.
        :type column_type: ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType

        :param description: Optional text that explains what this property represents.
        :type description: str, none_type, optional

        :param migration_metadata: Opaque metadata preserved when this property is migrated.
        :type migration_metadata: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param name: Name used to identify the property in the model.
        :type name: str
        """
        if description is not unset:
            kwargs["description"] = description
        if migration_metadata is not unset:
            kwargs["migration_metadata"] = migration_metadata
        super().__init__(kwargs)

        self_.column_name = column_name
        self_.column_type = column_type
        self_.name = name
