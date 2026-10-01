# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.archive_search_rehydration import ArchiveSearchRehydration
    from datadog_api_client.v2.model.archive_search_status import ArchiveSearchStatus


class ArchiveSearchResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.archive_search_rehydration import ArchiveSearchRehydration
        from datadog_api_client.v2.model.archive_search_status import ArchiveSearchStatus

        return {
            "archive_id": (str,),
            "bytes_scanned": (int,),
            "completed_at": (datetime,),
            "created_at": (datetime,),
            "description": (str,),
            "events_scanned": (int,),
            "expected_duration": (int,),
            "_from": (datetime,),
            "name": (str,),
            "query": (str,),
            "rehydration": (ArchiveSearchRehydration,),
            "status": (ArchiveSearchStatus,),
            "to": (datetime,),
        }

    attribute_map = {
        "archive_id": "archive_id",
        "bytes_scanned": "bytes_scanned",
        "completed_at": "completed_at",
        "created_at": "created_at",
        "description": "description",
        "events_scanned": "events_scanned",
        "expected_duration": "expected_duration",
        "_from": "from",
        "name": "name",
        "query": "query",
        "rehydration": "rehydration",
        "status": "status",
        "to": "to",
    }

    def __init__(
        self_,
        archive_id: str,
        bytes_scanned: int,
        created_at: datetime,
        events_scanned: int,
        _from: datetime,
        name: str,
        query: str,
        status: ArchiveSearchStatus,
        to: datetime,
        completed_at: Union[datetime, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        expected_duration: Union[int, UnsetType] = unset,
        rehydration: Union[ArchiveSearchRehydration, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an Archive Search.

        :param archive_id: ID of the archive being searched.
        :type archive_id: str

        :param bytes_scanned: Number of bytes read from the archive at the end of the search.
        :type bytes_scanned: int

        :param completed_at: Time the Archive Search finished, as an ISO 8601 timestamp.
            Absent while the search is still running.
        :type completed_at: datetime, optional

        :param created_at: Time the Archive Search was created, as an ISO 8601 timestamp.
        :type created_at: datetime

        :param description: Free-text description of the Archive Search.
        :type description: str, optional

        :param events_scanned: Number of events read from the archive at the end of the search.
        :type events_scanned: int

        :param expected_duration: Estimated time left before the Archive Search completes, in seconds.
        :type expected_duration: int, optional

        :param _from: Start of the searched time range, as an ISO 8601 timestamp.
        :type _from: datetime

        :param name: Name of the Archive Search.
        :type name: str

        :param query: Log search query used to filter the archived logs.
        :type query: str

        :param rehydration: Rehydration settings of the Archive Search. Absent when the search only scans the archive
            without indexing the results.
        :type rehydration: ArchiveSearchRehydration, optional

        :param status: Current state of an Archive Search.
        :type status: ArchiveSearchStatus

        :param to: End of the searched time range, as an ISO 8601 timestamp.
        :type to: datetime
        """
        if completed_at is not unset:
            kwargs["completed_at"] = completed_at
        if description is not unset:
            kwargs["description"] = description
        if expected_duration is not unset:
            kwargs["expected_duration"] = expected_duration
        if rehydration is not unset:
            kwargs["rehydration"] = rehydration
        super().__init__(kwargs)

        self_.archive_id = archive_id
        self_.bytes_scanned = bytes_scanned
        self_.created_at = created_at
        self_.events_scanned = events_scanned
        self_._from = _from
        self_.name = name
        self_.query = query
        self_.status = status
        self_.to = to
