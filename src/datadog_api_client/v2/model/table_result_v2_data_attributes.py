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
    from datadog_api_client.v2.model.table_result_v2_data_attributes_file_metadata import (
        TableResultV2DataAttributesFileMetadata,
    )
    from datadog_api_client.v2.model.table_result_v2_data_attributes_schema import TableResultV2DataAttributesSchema
    from datadog_api_client.v2.model.reference_table_source_type import ReferenceTableSourceType


class TableResultV2DataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.table_result_v2_data_attributes_file_metadata import (
            TableResultV2DataAttributesFileMetadata,
        )
        from datadog_api_client.v2.model.table_result_v2_data_attributes_schema import TableResultV2DataAttributesSchema
        from datadog_api_client.v2.model.reference_table_source_type import ReferenceTableSourceType

        return {
            "created_by": (str,),
            "description": (str,),
            "file_metadata": (TableResultV2DataAttributesFileMetadata,),
            "last_updated_by": (str,),
            "row_count": (int,),
            "schema": (TableResultV2DataAttributesSchema,),
            "source": (ReferenceTableSourceType,),
            "status": (str,),
            "table_name": (str,),
            "tags": ([str],),
            "updated_at": (str,),
        }

    attribute_map = {
        "created_by": "created_by",
        "description": "description",
        "file_metadata": "file_metadata",
        "last_updated_by": "last_updated_by",
        "row_count": "row_count",
        "schema": "schema",
        "source": "source",
        "status": "status",
        "table_name": "table_name",
        "tags": "tags",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        created_by: Union[str, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        file_metadata: Union[TableResultV2DataAttributesFileMetadata, UnsetType] = unset,
        last_updated_by: Union[str, UnsetType] = unset,
        row_count: Union[int, UnsetType] = unset,
        schema: Union[TableResultV2DataAttributesSchema, UnsetType] = unset,
        source: Union[ReferenceTableSourceType, UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        table_name: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        updated_at: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes that define the reference table's configuration and properties.

        :param created_by: UUID of the user who created the reference table.
        :type created_by: str, optional

        :param description: Optional text describing the purpose or contents of this reference table.
        :type description: str, optional

        :param file_metadata: Metadata specifying where and how to access the reference table's data file.

            For cloud storage tables (S3/GCS/Azure):

            * sync_enabled and access_details will always be present
            * error fields (error_message, error_row_count, error_type) are present only when errors occur

            For local file tables:

            * error fields (error_message, error_row_count) are present only when errors occur
            * sync_enabled, access_details are never present
        :type file_metadata: TableResultV2DataAttributesFileMetadata, optional

        :param last_updated_by: UUID of the user who last updated the reference table.
        :type last_updated_by: str, optional

        :param row_count: The number of successfully processed rows in the reference table.
        :type row_count: int, optional

        :param schema: Schema defining the structure and columns of the reference table.
        :type schema: TableResultV2DataAttributesSchema, optional

        :param source: The source type for reference table data. Includes all possible source types that can appear in responses.
        :type source: ReferenceTableSourceType, optional

        :param status: The processing status of the table.
        :type status: str, optional

        :param table_name: Unique name to identify this reference table. Used in enrichment processors and API calls.
        :type table_name: str, optional

        :param tags: Tags for organizing and filtering reference tables.
        :type tags: [str], optional

        :param updated_at: When the reference table was last updated, in ISO 8601 format.
        :type updated_at: str, optional
        """
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if description is not unset:
            kwargs["description"] = description
        if file_metadata is not unset:
            kwargs["file_metadata"] = file_metadata
        if last_updated_by is not unset:
            kwargs["last_updated_by"] = last_updated_by
        if row_count is not unset:
            kwargs["row_count"] = row_count
        if schema is not unset:
            kwargs["schema"] = schema
        if source is not unset:
            kwargs["source"] = source
        if status is not unset:
            kwargs["status"] = status
        if table_name is not unset:
            kwargs["table_name"] = table_name
        if tags is not unset:
            kwargs["tags"] = tags
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        super().__init__(kwargs)
