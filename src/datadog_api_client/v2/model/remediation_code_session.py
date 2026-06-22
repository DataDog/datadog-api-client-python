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
    from datadog_api_client.v2.model.remediation_pull_request_status import RemediationPullRequestStatus


class RemediationCodeSession(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.remediation_pull_request_status import RemediationPullRequestStatus

        return {
            "id": (str,),
            "pull_request_status": (RemediationPullRequestStatus,),
        }

    attribute_map = {
        "id": "id",
        "pull_request_status": "pull_request_status",
    }

    def __init__(
        self_,
        id: Union[str, UnsetType] = unset,
        pull_request_status: Union[RemediationPullRequestStatus, UnsetType] = unset,
        **kwargs,
    ):
        """
        A linked code session (for example, a pull request) for the investigation.

        :param id: Code session ID.
        :type id: str, optional

        :param pull_request_status: Pull request status for a linked code session.
        :type pull_request_status: RemediationPullRequestStatus, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if pull_request_status is not unset:
            kwargs["pull_request_status"] = pull_request_status
        super().__init__(kwargs)
