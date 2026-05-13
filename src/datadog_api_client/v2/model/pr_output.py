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
    from datadog_api_client.v2.model.pr_output_ci_status import PROutputCiStatus
    from datadog_api_client.v2.model.pr_output_status import PROutputStatus


class PROutput(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.pr_output_ci_status import PROutputCiStatus
        from datadog_api_client.v2.model.pr_output_status import PROutputStatus

        return {
            "ci_status": (PROutputCiStatus,),
            "pr_number": (int,),
            "pr_url": (str,),
            "repository": (str,),
            "status": (PROutputStatus,),
        }

    attribute_map = {
        "ci_status": "ci_status",
        "pr_number": "pr_number",
        "pr_url": "pr_url",
        "repository": "repository",
        "status": "status",
    }

    def __init__(
        self_,
        pr_url: str,
        ci_status: Union[PROutputCiStatus, UnsetType] = unset,
        pr_number: Union[int, UnsetType] = unset,
        repository: Union[str, UnsetType] = unset,
        status: Union[PROutputStatus, UnsetType] = unset,
        **kwargs,
    ):
        """
        A pull request created by the dependency upgrade automation.

        :param ci_status: The aggregate CI check status for the pull request.
        :type ci_status: PROutputCiStatus, optional

        :param pr_number: The pull request number.
        :type pr_number: int, optional

        :param pr_url: The URL of the pull request.
        :type pr_url: str

        :param repository: The repository name in owner/repo format.
        :type repository: str, optional

        :param status: The current status of the pull request.
        :type status: PROutputStatus, optional
        """
        if ci_status is not unset:
            kwargs["ci_status"] = ci_status
        if pr_number is not unset:
            kwargs["pr_number"] = pr_number
        if repository is not unset:
            kwargs["repository"] = repository
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)

        self_.pr_url = pr_url
