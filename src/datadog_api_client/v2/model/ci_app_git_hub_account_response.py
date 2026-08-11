# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ci_app_git_hub_account_data import CIAppGitHubAccountData


class CIAppGitHubAccountResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ci_app_git_hub_account_data import CIAppGitHubAccountData

        return {
            "data": (CIAppGitHubAccountData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CIAppGitHubAccountData, **kwargs):
        """
        Response object containing a single GitHub account's CI Visibility opt-in status.

        :param data: Data object for a GitHub account.
        :type data: CIAppGitHubAccountData
        """
        super().__init__(kwargs)

        self_.data = data
