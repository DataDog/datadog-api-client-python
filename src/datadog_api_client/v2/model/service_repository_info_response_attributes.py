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
    from datadog_api_client.v2.model.service_repository_info_status import ServiceRepositoryInfoStatus


class ServiceRepositoryInfoResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.service_repository_info_status import ServiceRepositoryInfoStatus

        return {
            "commit_sha": (str,),
            "repository_url": (str,),
            "status": (ServiceRepositoryInfoStatus,),
        }

    attribute_map = {
        "commit_sha": "commit_sha",
        "repository_url": "repository_url",
        "status": "status",
    }

    def __init__(
        self_,
        status: ServiceRepositoryInfoStatus,
        commit_sha: Union[str, UnsetType] = unset,
        repository_url: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the service repository information.

        :param commit_sha: The SHA of the commit associated with the service version.
        :type commit_sha: str, optional

        :param repository_url: The URL of the source code repository.
        :type repository_url: str, optional

        :param status: The status of the service repository info lookup.
        :type status: ServiceRepositoryInfoStatus
        """
        if commit_sha is not unset:
            kwargs["commit_sha"] = commit_sha
        if repository_url is not unset:
            kwargs["repository_url"] = repository_url
        super().__init__(kwargs)

        self_.status = status
