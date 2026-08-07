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
    from datadog_api_client.v2.model.ci_app_git_hub_account_update_request_repository import (
        CIAppGitHubAccountUpdateRequestRepository,
    )


class CIAppGitHubAccountUpdateRequestAttributes(ModelNormal):
    validations = {
        "account": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ci_app_git_hub_account_update_request_repository import (
            CIAppGitHubAccountUpdateRequestRepository,
        )

        return {
            "account": (str,),
            "enabled": (bool,),
            "host": (str,),
            "repository": (CIAppGitHubAccountUpdateRequestRepository,),
        }

    attribute_map = {
        "account": "account",
        "enabled": "enabled",
        "host": "host",
        "repository": "repository",
    }

    def __init__(
        self_,
        account: str,
        enabled: Union[bool, UnsetType] = unset,
        host: Union[str, UnsetType] = unset,
        repository: Union[CIAppGitHubAccountUpdateRequestRepository, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for updating a GitHub account's CI Visibility opt-in status.
        At least one of ``enabled`` or ``repository.enabled`` must be provided.
        Account-level and repository-level opt-in changes are independent and may both be supplied in the same request.

        :param account: The GitHub account (organization or user) name to update, identified by name.
        :type account: str

        :param enabled: Whether to enable or disable CI Visibility at the account level.
        :type enabled: bool, optional

        :param host: The GitHub host ( ``github.com`` or a GHES hostname) the account belongs to. Required to disambiguate
            when the same account name exists on more than one host.
        :type host: str, optional

        :param repository: Repository-level opt-in change to apply, identified by name.
        :type repository: CIAppGitHubAccountUpdateRequestRepository, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if host is not unset:
            kwargs["host"] = host
        if repository is not unset:
            kwargs["repository"] = repository
        super().__init__(kwargs)

        self_.account = account
