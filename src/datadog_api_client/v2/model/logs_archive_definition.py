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


from datadog_api_client.v2.model.logs_archive_destination import LogsArchiveDestination
from datadog_api_client.v2.model.logs_archive_state import LogsArchiveState
from datadog_api_client.v2.model.logs_archive_attributes import LogsArchiveAttributes
from datadog_api_client.v2.model.logs_archive_destination import LogsArchiveDestination
from datadog_api_client.v2.model.logs_archive_destination_azure import LogsArchiveDestinationAzure
from datadog_api_client.v2.model.logs_archive_destination_gcs import LogsArchiveDestinationGCS
from datadog_api_client.v2.model.logs_archive_destination_s3 import LogsArchiveDestinationS3
from datadog_api_client.v2.model.logs_archive_state import LogsArchiveState


@dataclass
class LogsArchiveDefinitionJSON:
    id: str
    destination: Union[
        Union[LogsArchiveDestination, LogsArchiveDestinationAzure, LogsArchiveDestinationGCS, LogsArchiveDestinationS3],
        none_type,
        UnsetType,
    ] = unset
    include_tags: Union[bool, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    query: Union[str, UnsetType] = unset
    rehydration_max_scan_size_in_gb: Union[int, none_type, UnsetType] = unset
    rehydration_tags: Union[List[str], UnsetType] = unset
    state: Union[LogsArchiveState, UnsetType] = unset


class LogsArchiveDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "attributes": (LogsArchiveAttributes,),
            "id": (str,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    read_only_vars = {
        "id",
        "type",
    }
    json_api_model = LogsArchiveDefinitionJSON

    def __init__(
        self_, attributes: Union[LogsArchiveAttributes, UnsetType] = unset, id: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        The definition of an archive.

        :param attributes: The attributes associated with the archive.
        :type attributes: LogsArchiveAttributes, optional

        :param id: The archive ID.
        :type id: str, optional

        :param type: The type of the resource. The value should always be archives.
        :type type: str
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)
        type = kwargs.get("type", "archives")

        self_.type = type
