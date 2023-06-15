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


from datadog_api_client.v2.model.logs_archive_create_request_destination import LogsArchiveCreateRequestDestination
from datadog_api_client.v2.model.logs_archive_create_request_destination import LogsArchiveCreateRequestDestination
from datadog_api_client.v2.model.logs_archive_destination_azure import LogsArchiveDestinationAzure
from datadog_api_client.v2.model.logs_archive_destination_gcs import LogsArchiveDestinationGCS
from datadog_api_client.v2.model.logs_archive_destination_s3 import LogsArchiveDestinationS3

if TYPE_CHECKING:
    from datadog_api_client.v2.model.logs_archive_create_request_definition import LogsArchiveCreateRequestDefinition


@dataclass
class LogsArchiveCreateRequestJSON:
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


class LogsArchiveCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.logs_archive_create_request_definition import (
            LogsArchiveCreateRequestDefinition,
        )

        return {
            "data": (LogsArchiveCreateRequestDefinition,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = LogsArchiveCreateRequestJSON

    def __init__(self_, data: Union[LogsArchiveCreateRequestDefinition, UnsetType] = unset, **kwargs):
        """
        The logs archive.

        :param data: The definition of an archive.
        :type data: LogsArchiveCreateRequestDefinition, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
