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
    from datadog_api_client.v2.model.ci_app_git_hub_account_attributes import CIAppGitHubAccountAttributes
    from datadog_api_client.v2.model.ci_app_git_hub_account_type import CIAppGitHubAccountType


class CIAppGitHubAccountData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ci_app_git_hub_account_attributes import CIAppGitHubAccountAttributes
        from datadog_api_client.v2.model.ci_app_git_hub_account_type import CIAppGitHubAccountType

        return {
            "attributes": (CIAppGitHubAccountAttributes,),
            "id": (str,),
            "type": (CIAppGitHubAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: CIAppGitHubAccountAttributes, id: str, type: CIAppGitHubAccountType, **kwargs):
        """
        Data object for a GitHub account.

        :param attributes: Attributes describing a GitHub account's CI Visibility opt-in status.
        :type attributes: CIAppGitHubAccountAttributes

        :param id: The account's unique identifier, in the form ``<host>/<account name>``
            (for example ``github.com/datadog`` ).
        :type id: str

        :param type: JSON:API type for the GitHub account resource.
            The value must always be ``ci_github_account``.
        :type type: CIAppGitHubAccountType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
