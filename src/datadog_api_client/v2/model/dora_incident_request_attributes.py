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
    from datadog_api_client.v2.model.dora_git_info import DORAGitInfo


class DORAIncidentRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dora_git_info import DORAGitInfo

        return {
            "finished_at": (int,),
            "git": (DORAGitInfo,),
            "id": (str,),
            "name": (str,),
            "service": (str,),
            "severity": (str,),
            "started_at": (int,),
            "version": (str,),
        }

    attribute_map = {
        "finished_at": "finished_at",
        "git": "git",
        "id": "id",
        "name": "name",
        "service": "service",
        "severity": "severity",
        "started_at": "started_at",
        "version": "version",
    }

    def __init__(
        self_,
        service: str,
        started_at: int,
        finished_at: Union[int, UnsetType] = unset,
        git: Union[DORAGitInfo, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        severity: Union[str, UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes to create a DORA incident event.

        :param finished_at: Unix timestamp in nanoseconds when the incident finished. It should not be older than 3 hours.
        :type finished_at: int, optional

        :param git: Git info for DORA Metrics events.
        :type git: DORAGitInfo, optional

        :param id: Incident ID
        :type id: str, optional

        :param name: Incident name.
        :type name: str, optional

        :param service: Service name from a service available in the Service Catalog.
        :type service: str

        :param severity: Incident severity.
        :type severity: str, optional

        :param started_at: Unix timestamp in nanoseconds when the incident started.
        :type started_at: int

        :param version: Version to correlate with `APM Deployment Tracking <https://docs.datadoghq.com/tracing/services/deployment_tracking/>`_.
        :type version: str, optional
        """
        if finished_at is not unset:
            kwargs["finished_at"] = finished_at
        if git is not unset:
            kwargs["git"] = git
        if id is not unset:
            kwargs["id"] = id
        if name is not unset:
            kwargs["name"] = name
        if severity is not unset:
            kwargs["severity"] = severity
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)

        self_.service = service
        self_.started_at = started_at
