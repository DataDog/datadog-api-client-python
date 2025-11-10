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
    from datadog_api_client.v2.model.create_table_request_data_attributes_file_metadata import (
        CreateTableRequestDataAttributesFileMetadata,
    )
    from datadog_api_client.v2.model.create_table_request_data_attributes_schema import (
        CreateTableRequestDataAttributesSchema,
    )
    from datadog_api_client.v2.model.reference_table_create_source_type import ReferenceTableCreateSourceType
    from datadog_api_client.v2.model.create_table_request_data_attributes_file_metadata_cloud_storage import (
        CreateTableRequestDataAttributesFileMetadataCloudStorage,
    )
    from datadog_api_client.v2.model.create_table_request_data_attributes_file_metadata_local_file import (
        CreateTableRequestDataAttributesFileMetadataLocalFile,
    )


class CreateTableRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_table_request_data_attributes_file_metadata import (
            CreateTableRequestDataAttributesFileMetadata,
        )
        from datadog_api_client.v2.model.create_table_request_data_attributes_schema import (
            CreateTableRequestDataAttributesSchema,
        )
        from datadog_api_client.v2.model.reference_table_create_source_type import ReferenceTableCreateSourceType

        return {
            "description": (str,),
            "file_metadata": (CreateTableRequestDataAttributesFileMetadata,),
            "schema": (CreateTableRequestDataAttributesSchema,),
            "source": (ReferenceTableCreateSourceType,),
            "table_name": (str,),
            "tags": ([str],),
        }

    attribute_map = {
        "description": "description",
        "file_metadata": "file_metadata",
        "schema": "schema",
        "source": "source",
        "table_name": "table_name",
        "tags": "tags",
    }

    def __init__(
        self_,
        schema: CreateTableRequestDataAttributesSchema,
        source: ReferenceTableCreateSourceType,
        table_name: str,
        description: Union[str, UnsetType] = unset,
        file_metadata: Union[
            CreateTableRequestDataAttributesFileMetadata,
            CreateTableRequestDataAttributesFileMetadataCloudStorage,
            CreateTableRequestDataAttributesFileMetadataLocalFile,
            UnsetType,
        ] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes that define the reference table's configuration and properties.

        :param description: Optional text describing the purpose or contents of this reference table.
        :type description: str, optional

        :param file_metadata: Metadata specifying where and how to access the reference table's data file.
        :type file_metadata: CreateTableRequestDataAttributesFileMetadata, optional

        :param schema: Schema defining the structure and columns of the reference table.
        :type schema: CreateTableRequestDataAttributesSchema

        :param source: The source type for creating reference table data. Only these source types can be created through this API.
        :type source: ReferenceTableCreateSourceType

        :param table_name: Name to identify this reference table.
        :type table_name: str

        :param tags: Tags for organizing and filtering reference tables.
        :type tags: [str], optional
        """
        if description is not unset:
            kwargs["description"] = description
        if file_metadata is not unset:
            kwargs["file_metadata"] = file_metadata
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.schema = schema
        self_.source = source
        self_.table_name = table_name
