# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.logs_archive_destination import LogsArchiveDestination
from datadog_api_client.v2.model.logs_archive_state import LogsArchiveState
from datadog_api_client.v2.model.logs_archive_destination import LogsArchiveDestination
from datadog_api_client.v2.model.logs_archive_destination_azure import LogsArchiveDestinationAzure
from datadog_api_client.v2.model.logs_archive_destination_gcs import LogsArchiveDestinationGCS
from datadog_api_client.v2.model.logs_archive_destination_s3 import LogsArchiveDestinationS3
from datadog_api_client.v2.model.logs_archive_state import LogsArchiveState

if TYPE_CHECKING:
    from datadog_api_client.v2.model.logs_archive_definition import LogsArchiveDefinition


@dataclass
class LogsArchiveJSON:
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


class LogsArchive(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.logs_archive_definition import LogsArchiveDefinition

        return {
            "data": (LogsArchiveDefinition,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = LogsArchiveJSON

    def __init__(self_, data: Union[LogsArchiveDefinition, UnsetType] = unset, **kwargs):
        """
        The logs archive.

        :param data: The definition of an archive.
        :type data: LogsArchiveDefinition, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
