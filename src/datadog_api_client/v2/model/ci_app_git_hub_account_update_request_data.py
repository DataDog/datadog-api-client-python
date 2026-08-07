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
    from datadog_api_client.v2.model.ci_app_git_hub_account_update_request_attributes import (
        CIAppGitHubAccountUpdateRequestAttributes,
    )
    from datadog_api_client.v2.model.ci_app_git_hub_account_type import CIAppGitHubAccountType


class CIAppGitHubAccountUpdateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ci_app_git_hub_account_update_request_attributes import (
            CIAppGitHubAccountUpdateRequestAttributes,
        )
        from datadog_api_client.v2.model.ci_app_git_hub_account_type import CIAppGitHubAccountType

        return {
            "attributes": (CIAppGitHubAccountUpdateRequestAttributes,),
            "type": (CIAppGitHubAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: CIAppGitHubAccountUpdateRequestAttributes, type: CIAppGitHubAccountType, **kwargs):
        """
        Data object for updating a GitHub account's CI Visibility opt-in status.

        :param attributes: Attributes for updating a GitHub account's CI Visibility opt-in status.
            At least one of ``enabled`` or ``repository.enabled`` must be provided.
            Account-level and repository-level opt-in changes are independent and may both be supplied in the same request.
        :type attributes: CIAppGitHubAccountUpdateRequestAttributes

        :param type: JSON:API type for the GitHub account resource.
            The value must always be ``ci_github_account``.
        :type type: CIAppGitHubAccountType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
