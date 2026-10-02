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
    from datadog_api_client.v2.model.experiments_metric_sql_model_v2_dto_data_attributes_measures_items import (
        ExperimentsMetricSQLModelV2DTODataAttributesMeasuresItems,
    )
    from datadog_api_client.v2.model.experiments_metric_sql_model_v2_dto_data_attributes_subject_types_items import (
        ExperimentsMetricSQLModelV2DTODataAttributesSubjectTypesItems,
    )


class ExperimentsMetricSQLModelV2DTODataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_metric_sql_model_v2_dto_data_attributes_measures_items import (
            ExperimentsMetricSQLModelV2DTODataAttributesMeasuresItems,
        )
        from datadog_api_client.v2.model.experiments_metric_sql_model_v2_dto_data_attributes_subject_types_items import (
            ExperimentsMetricSQLModelV2DTODataAttributesSubjectTypesItems,
        )

        return {
            "certified_at": (datetime, none_type),
            "created_at": (datetime,),
            "date_partition_column": (str, none_type),
            "description": (str, none_type),
            "event_count_measure_id": (str,),
            "experiment_count": (int, none_type),
            "is_certified": (bool,),
            "measures": ([ExperimentsMetricSQLModelV2DTODataAttributesMeasuresItems],),
            "metric_count": (int, none_type),
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
            "properties": ([ExperimentsMetricSQLModelV2DTODataAttributesMeasuresItems],),
            "sql": (str,),
            "subject_types": ([ExperimentsMetricSQLModelV2DTODataAttributesSubjectTypesItems],),
            "timestamp_column": (str,),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "certified_at": "certified_at",
        "created_at": "created_at",
        "date_partition_column": "date_partition_column",
        "description": "description",
        "event_count_measure_id": "event_count_measure_id",
        "experiment_count": "experiment_count",
        "is_certified": "is_certified",
        "measures": "measures",
        "metric_count": "metric_count",
        "migration_metadata": "migration_metadata",
        "name": "name",
        "properties": "properties",
        "sql": "sql",
        "subject_types": "subject_types",
        "timestamp_column": "timestamp_column",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        certified_at: Union[datetime, none_type, UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        date_partition_column: Union[str, none_type, UnsetType] = unset,
        description: Union[str, none_type, UnsetType] = unset,
        event_count_measure_id: Union[str, UnsetType] = unset,
        experiment_count: Union[int, none_type, UnsetType] = unset,
        is_certified: Union[bool, UnsetType] = unset,
        measures: Union[List[ExperimentsMetricSQLModelV2DTODataAttributesMeasuresItems], UnsetType] = unset,
        metric_count: Union[int, none_type, UnsetType] = unset,
        migration_metadata: Union[Any, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        properties: Union[List[ExperimentsMetricSQLModelV2DTODataAttributesMeasuresItems], UnsetType] = unset,
        sql: Union[str, UnsetType] = unset,
        subject_types: Union[List[ExperimentsMetricSQLModelV2DTODataAttributesSubjectTypesItems], UnsetType] = unset,
        timestamp_column: Union[str, UnsetType] = unset,
        updated_at: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        Details of the metric SQL model.

        :param certified_at: Time when this resource was certified.
        :type certified_at: datetime, none_type, optional

        :param created_at: Time when this resource was created.
        :type created_at: datetime, optional

        :param date_partition_column: SQL column used to partition the source data by date.
        :type date_partition_column: str, none_type, optional

        :param description: Text that explains the metric SQL model.
        :type description: str, none_type, optional

        :param event_count_measure_id: Read-only measure ID. Pass it as warehouse_metric_measure.id when the metric operation is count.
        :type event_count_measure_id: str, optional

        :param experiment_count: Number of experiments that reference this resource.
        :type experiment_count: int, none_type, optional

        :param is_certified: Whether this resource has been certified.
        :type is_certified: bool, optional

        :param measures: Measures available from the SQL model's result columns.
        :type measures: [ExperimentsMetricSQLModelV2DTODataAttributesMeasuresItems], optional

        :param metric_count: Number of metrics that use this SQL model.
        :type metric_count: int, none_type, optional

        :param migration_metadata: Metadata retained for resources imported from another system.
        :type migration_metadata: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param name: Display name of the metric SQL model.
        :type name: str, optional

        :param properties: Property columns exposed by the SQL model.
        :type properties: [ExperimentsMetricSQLModelV2DTODataAttributesMeasuresItems], optional

        :param sql: SQL query that produces the model's source data.
        :type sql: str, optional

        :param subject_types: Subject types mapped to columns in the SQL model.
        :type subject_types: [ExperimentsMetricSQLModelV2DTODataAttributesSubjectTypesItems], optional

        :param timestamp_column: SQL column that supplies the event timestamp.
        :type timestamp_column: str, optional

        :param updated_at: Time when this resource was last updated.
        :type updated_at: datetime, optional
        """
        if certified_at is not unset:
            kwargs["certified_at"] = certified_at
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if date_partition_column is not unset:
            kwargs["date_partition_column"] = date_partition_column
        if description is not unset:
            kwargs["description"] = description
        if event_count_measure_id is not unset:
            kwargs["event_count_measure_id"] = event_count_measure_id
        if experiment_count is not unset:
            kwargs["experiment_count"] = experiment_count
        if is_certified is not unset:
            kwargs["is_certified"] = is_certified
        if measures is not unset:
            kwargs["measures"] = measures
        if metric_count is not unset:
            kwargs["metric_count"] = metric_count
        if migration_metadata is not unset:
            kwargs["migration_metadata"] = migration_metadata
        if name is not unset:
            kwargs["name"] = name
        if properties is not unset:
            kwargs["properties"] = properties
        if sql is not unset:
            kwargs["sql"] = sql
        if subject_types is not unset:
            kwargs["subject_types"] = subject_types
        if timestamp_column is not unset:
            kwargs["timestamp_column"] = timestamp_column
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        super().__init__(kwargs)
