# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.logs_archive_create_request_destination import LogsArchiveCreateRequestDestination
from datadog_api_client.v2.model.logs_archive_create_request_attributes import LogsArchiveCreateRequestAttributes
from datadog_api_client.v2.model.logs_archive_create_request_destination import LogsArchiveCreateRequestDestination
from datadog_api_client.v2.model.logs_archive_destination_azure import LogsArchiveDestinationAzure
from datadog_api_client.v2.model.logs_archive_destination_gcs import LogsArchiveDestinationGCS
from datadog_api_client.v2.model.logs_archive_destination_s3 import LogsArchiveDestinationS3


@dataclass
class LogsArchiveCreateRequestDefinitionJSON:
    destination: Union[
        LogsArchiveCreateRequestDestination,
        LogsArchiveDestinationAzure,
        LogsArchiveDestinationGCS,
        LogsArchiveDestinationS3,
        UnsetType,
    ] = unset
    include_tags: Union[bool, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    query: Union[str, UnsetType] = unset
    rehydration_max_scan_size_in_gb: Union[int, none_type, UnsetType] = unset
    rehydration_tags: Union[List[str], UnsetType] = unset


class LogsArchiveCreateRequestDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "attributes": (LogsArchiveCreateRequestAttributes,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }
    json_api_model = LogsArchiveCreateRequestDefinitionJSON

    def __init__(self_, attributes: Union[LogsArchiveCreateRequestAttributes, UnsetType] = unset, **kwargs):
        """
        The definition of an archive.

        :param attributes: The attributes associated with the archive.
        :type attributes: LogsArchiveCreateRequestAttributes, optional

        :param type: The type of the resource. The value should always be archives.
        :type type: str
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)
        type = kwargs.get("type", "archives")

        self_.type = type
