# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List, Union, TYPE_CHECKING

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
    from datadog_api_client.v2.model.experiments_create_metric_sql_model_v2_request_data_attributes_measures_items import (
        ExperimentsCreateMetricSQLModelV2RequestDataAttributesMeasuresItems,
    )
    from datadog_api_client.v2.model.experiments_metric_sql_model_property_input import (
        ExperimentsMetricSQLModelPropertyInput,
    )
    from datadog_api_client.v2.model.experiments_create_exposure_sql_model_v2_request_data_attributes_subject_types_items import (
        ExperimentsCreateExposureSQLModelV2RequestDataAttributesSubjectTypesItems,
    )


class ExperimentsUpdateMetricSQLModelV2RequestDataAttributes(ModelNormal):
    validations = {
        "subject_types": {
            "max_items": 10,
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_create_metric_sql_model_v2_request_data_attributes_measures_items import (
            ExperimentsCreateMetricSQLModelV2RequestDataAttributesMeasuresItems,
        )
        from datadog_api_client.v2.model.experiments_metric_sql_model_property_input import (
            ExperimentsMetricSQLModelPropertyInput,
        )
        from datadog_api_client.v2.model.experiments_create_exposure_sql_model_v2_request_data_attributes_subject_types_items import (
            ExperimentsCreateExposureSQLModelV2RequestDataAttributesSubjectTypesItems,
        )

        return {
            "date_partition_column": (str, none_type),
            "description": (str, none_type),
            "measures": ([ExperimentsCreateMetricSQLModelV2RequestDataAttributesMeasuresItems],),
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
            "properties": ([ExperimentsMetricSQLModelPropertyInput],),
            "sql": (str,),
            "subject_types": ([ExperimentsCreateExposureSQLModelV2RequestDataAttributesSubjectTypesItems],),
            "timestamp_column": (str,),
        }

    attribute_map = {
        "date_partition_column": "date_partition_column",
        "description": "description",
        "measures": "measures",
        "migration_metadata": "migration_metadata",
        "name": "name",
        "properties": "properties",
        "sql": "sql",
        "subject_types": "subject_types",
        "timestamp_column": "timestamp_column",
    }

    def __init__(
        self_,
        name: str,
        sql: str,
        subject_types: List[ExperimentsCreateExposureSQLModelV2RequestDataAttributesSubjectTypesItems],
        timestamp_column: str,
        date_partition_column: Union[str, none_type, UnsetType] = unset,
        description: Union[str, none_type, UnsetType] = unset,
        measures: Union[List[ExperimentsCreateMetricSQLModelV2RequestDataAttributesMeasuresItems], UnsetType] = unset,
        migration_metadata: Union[Any, UnsetType] = unset,
        properties: Union[List[ExperimentsMetricSQLModelPropertyInput], UnsetType] = unset,
        **kwargs,
    ):
        """
        Complete column mappings and query used to replace the metric SQL model.

        :param date_partition_column: SQL column used to partition the source data by date.
        :type date_partition_column: str, none_type, optional

        :param description: Text that explains the metric SQL model.
        :type description: str, none_type, optional

        :param measures: Measures available from the SQL model's result columns.
        :type measures: [ExperimentsCreateMetricSQLModelV2RequestDataAttributesMeasuresItems], optional

        :param migration_metadata: Metadata retained for resources imported from another system.
        :type migration_metadata: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param name: Display name of the metric SQL model.
        :type name: str

        :param properties: Property columns exposed by the SQL model.
        :type properties: [ExperimentsMetricSQLModelPropertyInput], optional

        :param sql: SQL query that produces the model's source data.
        :type sql: str

        :param subject_types: Subject types mapped to columns in the SQL model.
        :type subject_types: [ExperimentsCreateExposureSQLModelV2RequestDataAttributesSubjectTypesItems]

        :param timestamp_column: SQL column that supplies the event timestamp.
        :type timestamp_column: str
        """
        if date_partition_column is not unset:
            kwargs["date_partition_column"] = date_partition_column
        if description is not unset:
            kwargs["description"] = description
        if measures is not unset:
            kwargs["measures"] = measures
        if migration_metadata is not unset:
            kwargs["migration_metadata"] = migration_metadata
        if properties is not unset:
            kwargs["properties"] = properties
        super().__init__(kwargs)

        self_.name = name
        self_.sql = sql
        self_.subject_types = subject_types
        self_.timestamp_column = timestamp_column
