# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.dora_deployment_averaged_metrics import DORADeploymentAveragedMetrics
    from datadog_api_client.v2.model.dora_git_info_response import DORAGitInfoResponse
    from datadog_api_client.v2.model.dora_deployment_remediation import DORADeploymentRemediation


class DORADeploymentObjectAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dora_deployment_averaged_metrics import DORADeploymentAveragedMetrics
        from datadog_api_client.v2.model.dora_git_info_response import DORAGitInfoResponse
        from datadog_api_client.v2.model.dora_deployment_remediation import DORADeploymentRemediation

        return {
            "ai": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "averaged_metrics": (DORADeploymentAveragedMetrics,),
            "change_failure": (bool,),
            "commits": (
                [
                    {
                        str: (
                            bool,
                            date,
                            datetime,
                            dict,
                            float,
                            int,
                            list,
                            str,
                            UUID,
                            none_type,
                        )
                    }
                ],
            ),
            "created_at": (datetime,),
            "custom": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "custom_tags": ([str],),
            "deployment_type": (str,),
            "duration": (int,),
            "env": (str,),
            "finished_at": (datetime,),
            "git": (DORAGitInfoResponse,),
            "number_of_commits": (int,),
            "number_of_pull_requests": (int,),
            "pull_requests": (
                [
                    {
                        str: (
                            bool,
                            date,
                            datetime,
                            dict,
                            float,
                            int,
                            list,
                            str,
                            UUID,
                            none_type,
                        )
                    }
                ],
            ),
            "recovery_time_sec": (int,),
            "remediation": (DORADeploymentRemediation,),
            "service": (str,),
            "source": (str,),
            "started_at": (datetime,),
            "team": (str,),
            "version": (str,),
        }

    attribute_map = {
        "ai": "ai",
        "averaged_metrics": "averaged_metrics",
        "change_failure": "change_failure",
        "commits": "commits",
        "created_at": "created_at",
        "custom": "custom",
        "custom_tags": "custom_tags",
        "deployment_type": "deployment_type",
        "duration": "duration",
        "env": "env",
        "finished_at": "finished_at",
        "git": "git",
        "number_of_commits": "number_of_commits",
        "number_of_pull_requests": "number_of_pull_requests",
        "pull_requests": "pull_requests",
        "recovery_time_sec": "recovery_time_sec",
        "remediation": "remediation",
        "service": "service",
        "source": "source",
        "started_at": "started_at",
        "team": "team",
        "version": "version",
    }

    def __init__(
        self_,
        service: str,
        started_at: datetime,
        ai: Union[Dict[str, Any], UnsetType] = unset,
        averaged_metrics: Union[DORADeploymentAveragedMetrics, UnsetType] = unset,
        change_failure: Union[bool, UnsetType] = unset,
        commits: Union[List[Dict[str, Any]], UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        custom: Union[Dict[str, Any], UnsetType] = unset,
        custom_tags: Union[List[str], none_type, UnsetType] = unset,
        deployment_type: Union[str, UnsetType] = unset,
        duration: Union[int, UnsetType] = unset,
        env: Union[str, UnsetType] = unset,
        finished_at: Union[datetime, UnsetType] = unset,
        git: Union[DORAGitInfoResponse, UnsetType] = unset,
        number_of_commits: Union[int, UnsetType] = unset,
        number_of_pull_requests: Union[int, UnsetType] = unset,
        pull_requests: Union[List[Dict[str, Any]], UnsetType] = unset,
        recovery_time_sec: Union[int, UnsetType] = unset,
        remediation: Union[DORADeploymentRemediation, UnsetType] = unset,
        source: Union[str, UnsetType] = unset,
        team: Union[str, UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of the deployment event.

        :param ai: AI-assisted development metrics aggregated across the commits and pull requests included in the deployment.
        :type ai: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param averaged_metrics: Averaged DORA and delivery metrics computed across the commits and pull requests included in the deployment.
        :type averaged_metrics: DORADeploymentAveragedMetrics, optional

        :param change_failure: Whether the deployment is flagged as a change failure.
        :type change_failure: bool, optional

        :param commits: The list of commits included in the deployment.
        :type commits: [{str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}], optional

        :param created_at: The time when the deployment event was recorded.
        :type created_at: datetime, optional

        :param custom: A map of custom metadata associated with the deployment.
        :type custom: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param custom_tags: A list of user-defined tags. The tags must follow the ``key:value`` pattern. Up to 100 may be added per event.
        :type custom_tags: [str], none_type, optional

        :param deployment_type: The type of the deployment.
        :type deployment_type: str, optional

        :param duration: The duration of the deployment.
        :type duration: int, optional

        :param env: Environment name to where the service was deployed.
        :type env: str, optional

        :param finished_at: The time when the deployment finished.
        :type finished_at: datetime, optional

        :param git: Git info returned by DORA Metrics events.
        :type git: DORAGitInfoResponse, optional

        :param number_of_commits: The number of commits associated with the deployment.
        :type number_of_commits: int, optional

        :param number_of_pull_requests: The number of pull requests associated with the deployment.
        :type number_of_pull_requests: int, optional

        :param pull_requests: The list of pull requests included in the deployment.
        :type pull_requests: [{str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}], optional

        :param recovery_time_sec: The recovery time, in seconds, for a deployment flagged as a change failure.
        :type recovery_time_sec: int, optional

        :param remediation: Remediation details for a deployment that was flagged as a change failure.
        :type remediation: DORADeploymentRemediation, optional

        :param service: Service name.
        :type service: str

        :param source: The source of the deployment event.
        :type source: str, optional

        :param started_at: The time when the deployment started.
        :type started_at: datetime

        :param team: Name of the team owning the deployed service.
        :type team: str, optional

        :param version: Version to correlate with APM Deployment Tracking.
        :type version: str, optional
        """
        if ai is not unset:
            kwargs["ai"] = ai
        if averaged_metrics is not unset:
            kwargs["averaged_metrics"] = averaged_metrics
        if change_failure is not unset:
            kwargs["change_failure"] = change_failure
        if commits is not unset:
            kwargs["commits"] = commits
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if custom is not unset:
            kwargs["custom"] = custom
        if custom_tags is not unset:
            kwargs["custom_tags"] = custom_tags
        if deployment_type is not unset:
            kwargs["deployment_type"] = deployment_type
        if duration is not unset:
            kwargs["duration"] = duration
        if env is not unset:
            kwargs["env"] = env
        if finished_at is not unset:
            kwargs["finished_at"] = finished_at
        if git is not unset:
            kwargs["git"] = git
        if number_of_commits is not unset:
            kwargs["number_of_commits"] = number_of_commits
        if number_of_pull_requests is not unset:
            kwargs["number_of_pull_requests"] = number_of_pull_requests
        if pull_requests is not unset:
            kwargs["pull_requests"] = pull_requests
        if recovery_time_sec is not unset:
            kwargs["recovery_time_sec"] = recovery_time_sec
        if remediation is not unset:
            kwargs["remediation"] = remediation
        if source is not unset:
            kwargs["source"] = source
        if team is not unset:
            kwargs["team"] = team
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)

        self_.service = service
        self_.started_at = started_at
