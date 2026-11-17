# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class GitHubCostsIntegrationAccountSettingsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "enterprise_name": (str,),
            "tags": (str,),
        }

    attribute_map = {
        "enterprise_name": "enterprise_name",
        "tags": "tags",
    }

    def __init__(self_, enterprise_name: str, tags: Union[str, UnsetType] = unset, **kwargs):
        """
        Settings configured on the GitHub Costs integration account.

        :param enterprise_name: Your GitHub enterprise slug, found on the enterprise settings page (e.g. enterprise-name), or an organization login (e.g. organization-name). An enterprise already covers every organization it owns.
        :type enterprise_name: str

        :param tags: Comma-separated tags added to the collected costs, for example ``env:prod,team:example``.
        :type tags: str, optional
        """
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.enterprise_name = enterprise_name
