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
    from datadog_api_client.v2.model.patch_table_request_data_attributes_file_metadata import (
        PatchTableRequestDataAttributesFileMetadata,
    )
    from datadog_api_client.v2.model.patch_table_request_data_attributes_schema import (
        PatchTableRequestDataAttributesSchema,
    )
    from datadog_api_client.v2.model.patch_table_request_data_attributes_file_metadata_cloud_storage import (
        PatchTableRequestDataAttributesFileMetadataCloudStorage,
    )
    from datadog_api_client.v2.model.patch_table_request_data_attributes_file_metadata_local_file import (
        PatchTableRequestDataAttributesFileMetadataLocalFile,
    )


class PatchTableRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.patch_table_request_data_attributes_file_metadata import (
            PatchTableRequestDataAttributesFileMetadata,
        )
        from datadog_api_client.v2.model.patch_table_request_data_attributes_schema import (
            PatchTableRequestDataAttributesSchema,
        )

        return {
            "description": (str,),
            "file_metadata": (PatchTableRequestDataAttributesFileMetadata,),
            "schema": (PatchTableRequestDataAttributesSchema,),
            "sync_enabled": (bool,),
            "tags": ([str],),
        }

    attribute_map = {
        "description": "description",
        "file_metadata": "file_metadata",
        "schema": "schema",
        "sync_enabled": "sync_enabled",
        "tags": "tags",
    }

    def __init__(
        self_,
        description: Union[str, UnsetType] = unset,
        file_metadata: Union[
            PatchTableRequestDataAttributesFileMetadata,
            PatchTableRequestDataAttributesFileMetadataCloudStorage,
            PatchTableRequestDataAttributesFileMetadataLocalFile,
            UnsetType,
        ] = unset,
        schema: Union[PatchTableRequestDataAttributesSchema, UnsetType] = unset,
        sync_enabled: Union[bool, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes that define the updates to the reference table's configuration and properties.

        :param description: Optional text describing the purpose or contents of this reference table.
        :type description: str, optional

        :param file_metadata: Metadata specifying where and how to access the reference table's data file.
        :type file_metadata: PatchTableRequestDataAttributesFileMetadata, optional

        :param schema: Schema defining the updates to the structure and columns of the reference table. Schema fields cannot be deleted or renamed.
        :type schema: PatchTableRequestDataAttributesSchema, optional

        :param sync_enabled: Whether this table is synced automatically.
        :type sync_enabled: bool, optional

        :param tags: Tags for organizing and filtering reference tables.
        :type tags: [str], optional
        """
        if description is not unset:
            kwargs["description"] = description
        if file_metadata is not unset:
            kwargs["file_metadata"] = file_metadata
        if schema is not unset:
            kwargs["schema"] = schema
        if sync_enabled is not unset:
            kwargs["sync_enabled"] = sync_enabled
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
