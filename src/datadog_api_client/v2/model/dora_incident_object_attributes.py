# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.dora_git_info import DORAGitInfo


class DORAIncidentObjectAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dora_git_info import DORAGitInfo

        return {
            "custom_tags": ([str],),
            "env": (str,),
            "finished_at": (datetime,),
            "git": (DORAGitInfo,),
            "name": (str,),
            "services": ([str],),
            "severity": (str,),
            "started_at": (datetime,),
            "team": (str,),
            "version": (str,),
        }

    attribute_map = {
        "custom_tags": "custom_tags",
        "env": "env",
        "finished_at": "finished_at",
        "git": "git",
        "name": "name",
        "services": "services",
        "severity": "severity",
        "started_at": "started_at",
        "team": "team",
        "version": "version",
    }

    def __init__(
        self_,
        custom_tags: Union[List[str], none_type, UnsetType] = unset,
        env: Union[str, UnsetType] = unset,
        finished_at: Union[datetime, UnsetType] = unset,
        git: Union[DORAGitInfo, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        services: Union[List[str], UnsetType] = unset,
        severity: Union[str, UnsetType] = unset,
        started_at: Union[datetime, UnsetType] = unset,
        team: Union[str, UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of the incident event.

        :param custom_tags: A list of user-defined tags. The tags must follow the ``key:value`` pattern. Up to 100 may be added per event.
        :type custom_tags: [str], none_type, optional

        :param env: Environment name that was impacted by the incident.
        :type env: str, optional

        :param finished_at: The time when the incident finished.
        :type finished_at: datetime, optional

        :param git: Git info for DORA Metrics events.
        :type git: DORAGitInfo, optional

        :param name: Incident name.
        :type name: str, optional

        :param services: Service names impacted by the incident.
        :type services: [str], optional

        :param severity: Incident severity.
        :type severity: str, optional

        :param started_at: The time when the incident started.
        :type started_at: datetime, optional

        :param team: Name of the team owning the services impacted.
        :type team: str, optional

        :param version: Version to correlate with APM Deployment Tracking.
        :type version: str, optional
        """
        if custom_tags is not unset:
            kwargs["custom_tags"] = custom_tags
        if env is not unset:
            kwargs["env"] = env
        if finished_at is not unset:
            kwargs["finished_at"] = finished_at
        if git is not unset:
            kwargs["git"] = git
        if name is not unset:
            kwargs["name"] = name
        if services is not unset:
            kwargs["services"] = services
        if severity is not unset:
            kwargs["severity"] = severity
        if started_at is not unset:
            kwargs["started_at"] = started_at
        if team is not unset:
            kwargs["team"] = team
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
