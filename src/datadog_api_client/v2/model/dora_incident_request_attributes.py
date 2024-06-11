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
    from datadog_api_client.v2.model.dora_git_info import DORAGitInfo


class DORAIncidentRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dora_git_info import DORAGitInfo

        return {
            "env": (str,),
            "finished_at": (int,),
            "git": (DORAGitInfo,),
            "id": (str,),
            "name": (str,),
            "services": ([str],),
            "severity": (str,),
            "started_at": (int,),
            "team": (str,),
            "version": (str,),
        }

    attribute_map = {
        "env": "env",
        "finished_at": "finished_at",
        "git": "git",
        "id": "id",
        "name": "name",
        "services": "services",
        "severity": "severity",
        "started_at": "started_at",
        "team": "team",
        "version": "version",
    }

    def __init__(
        self_,
        started_at: int,
        env: Union[str, UnsetType] = unset,
        finished_at: Union[int, UnsetType] = unset,
        git: Union[DORAGitInfo, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        services: Union[List[str], UnsetType] = unset,
        severity: Union[str, UnsetType] = unset,
        team: Union[str, UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes to create a DORA incident event.

        :param env: Environment name that was impacted by the incident.
        :type env: str, optional

        :param finished_at: Unix timestamp in nanoseconds when the incident finished. It should not be older than 1 hour.
        :type finished_at: int, optional

        :param git: Git info for DORA Metrics events.
        :type git: DORAGitInfo, optional

        :param id: Incident ID. Required to update a previously sent incident.
        :type id: str, optional

        :param name: Incident name.
        :type name: str, optional

        :param services: Service names impacted by the incident. If possible, use names registered in the Service Catalog. Required when the team field is not provided.
        :type services: [str], optional

        :param severity: Incident severity.
        :type severity: str, optional

        :param started_at: Unix timestamp in nanoseconds when the incident started.
        :type started_at: int

        :param team: Name of the team owning the services impacted. If possible, use team handles registered in Datadog. Required when the services field is not provided.
        :type team: str, optional

        :param version: Version to correlate with `APM Deployment Tracking <https://docs.datadoghq.com/tracing/services/deployment_tracking/>`_.
        :type version: str, optional
        """
        if env is not unset:
            kwargs["env"] = env
        if finished_at is not unset:
            kwargs["finished_at"] = finished_at
        if git is not unset:
            kwargs["git"] = git
        if id is not unset:
            kwargs["id"] = id
        if name is not unset:
            kwargs["name"] = name
        if services is not unset:
            kwargs["services"] = services
        if severity is not unset:
            kwargs["severity"] = severity
        if team is not unset:
            kwargs["team"] = team
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)

        self_.started_at = started_at
