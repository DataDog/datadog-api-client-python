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
    from datadog_api_client.v2.model.patch_table_request_data_attributes_file_metadata_one_of_access_details import (
        PatchTableRequestDataAttributesFileMetadataOneOfAccessDetails,
    )


class PatchTableRequestDataAttributesFileMetadataCloudStorage(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.patch_table_request_data_attributes_file_metadata_one_of_access_details import (
            PatchTableRequestDataAttributesFileMetadataOneOfAccessDetails,
        )

        return {
            "access_details": (PatchTableRequestDataAttributesFileMetadataOneOfAccessDetails,),
            "sync_enabled": (bool,),
        }

    attribute_map = {
        "access_details": "access_details",
        "sync_enabled": "sync_enabled",
    }

    def __init__(
        self_,
        access_details: Union[PatchTableRequestDataAttributesFileMetadataOneOfAccessDetails, UnsetType] = unset,
        sync_enabled: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Cloud storage file metadata for patch requests. Allows partial updates of access_details and sync_enabled.

        :param access_details: Cloud storage access configuration for the reference table data file.
        :type access_details: PatchTableRequestDataAttributesFileMetadataOneOfAccessDetails, optional

        :param sync_enabled: Whether this table is synced automatically.
        :type sync_enabled: bool, optional
        """
        if access_details is not unset:
            kwargs["access_details"] = access_details
        if sync_enabled is not unset:
            kwargs["sync_enabled"] = sync_enabled
        super().__init__(kwargs)
