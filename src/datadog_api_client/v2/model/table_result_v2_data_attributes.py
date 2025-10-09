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
    from datadog_api_client.v2.model.table_result_v2_data_attributes_file_metadata_cloud_storage import (
        TableResultV2DataAttributesFileMetadataCloudStorage,
    )
    from datadog_api_client.v2.model.table_result_v2_data_attributes_file_metadata_local_file import (
        TableResultV2DataAttributesFileMetadataLocalFile,
    )


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
        file_metadata: Union[
            TableResultV2DataAttributesFileMetadata,
            TableResultV2DataAttributesFileMetadataCloudStorage,
            TableResultV2DataAttributesFileMetadataLocalFile,
            UnsetType,
        ] = unset,
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
        The definition of ``TableResultV2DataAttributes`` object.

        :param created_by: UUID of the user who created the reference table.
        :type created_by: str, optional

        :param description: The description of the reference table.
        :type description: str, optional

        :param file_metadata: The definition of ``TableResultV2DataAttributesFileMetadata`` object.
        :type file_metadata: TableResultV2DataAttributesFileMetadata, optional

        :param last_updated_by: UUID of the user who last updated the reference table.
        :type last_updated_by: str, optional

        :param row_count: The number of successfully processed rows in the reference table.
        :type row_count: int, optional

        :param schema: The definition of ``TableResultV2DataAttributesSchema`` object.
        :type schema: TableResultV2DataAttributesSchema, optional

        :param source: The source type for reference table data. Includes all possible source types that can appear in responses.
        :type source: ReferenceTableSourceType, optional

        :param status: The status of the reference table.
        :type status: str, optional

        :param table_name: The name of the reference table.
        :type table_name: str, optional

        :param tags: The tags of the reference table.
        :type tags: [str], optional

        :param updated_at: The timestamp of the last update to the reference table in ISO 8601 format.
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
