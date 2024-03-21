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


class DORADeploymentRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dora_git_info import DORAGitInfo

        return {
            "env": (str,),
            "finished_at": (int,),
            "git": (DORAGitInfo,),
            "id": (str,),
            "service": (str,),
            "started_at": (int,),
            "version": (str,),
        }

    attribute_map = {
        "env": "env",
        "finished_at": "finished_at",
        "git": "git",
        "id": "id",
        "service": "service",
        "started_at": "started_at",
        "version": "version",
    }

    def __init__(
        self_,
        finished_at: int,
        service: str,
        started_at: int,
        env: Union[str, UnsetType] = unset,
        git: Union[DORAGitInfo, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes to create a DORA deployment event.

        :param env: Environment name to where the service was deployed.
        :type env: str, optional

        :param finished_at: Unix timestamp in nanoseconds when the deployment finished. It should not be older than 1 hour.
        :type finished_at: int

        :param git: Git info for DORA Metrics events.
        :type git: DORAGitInfo, optional

        :param id: Deployment ID.
        :type id: str, optional

        :param service: Service name from a service available in the Service Catalog.
        :type service: str

        :param started_at: Unix timestamp in nanoseconds when the deployment started.
        :type started_at: int

        :param version: Version to correlate with `APM Deployment Tracking <https://docs.datadoghq.com/tracing/services/deployment_tracking/>`_.
        :type version: str, optional
        """
        if env is not unset:
            kwargs["env"] = env
        if git is not unset:
            kwargs["git"] = git
        if id is not unset:
            kwargs["id"] = id
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)

        self_.finished_at = finished_at
        self_.service = service
        self_.started_at = started_at
