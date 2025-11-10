# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.create_table_request_data_attributes_file_metadata_one_of_access_details import (
        CreateTableRequestDataAttributesFileMetadataOneOfAccessDetails,
    )


class CreateTableRequestDataAttributesFileMetadataCloudStorage(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_table_request_data_attributes_file_metadata_one_of_access_details import (
            CreateTableRequestDataAttributesFileMetadataOneOfAccessDetails,
        )

        return {
            "access_details": (CreateTableRequestDataAttributesFileMetadataOneOfAccessDetails,),
            "sync_enabled": (bool,),
        }

    attribute_map = {
        "access_details": "access_details",
        "sync_enabled": "sync_enabled",
    }

    def __init__(
        self_,
        access_details: CreateTableRequestDataAttributesFileMetadataOneOfAccessDetails,
        sync_enabled: bool,
        **kwargs,
    ):
        """
        Cloud storage file metadata for create requests. Both access_details and sync_enabled are required.

        :param access_details: Cloud storage access configuration for the reference table data file.
        :type access_details: CreateTableRequestDataAttributesFileMetadataOneOfAccessDetails

        :param sync_enabled: Whether this table is synced automatically.
        :type sync_enabled: bool
        """
        super().__init__(kwargs)

        self_.access_details = access_details
        self_.sync_enabled = sync_enabled
