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


class GitHubCostsIntegrationAccountSettingsUpdate(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

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

    def __init__(self_, enterprise_name: Union[str, UnsetType] = unset, tags: Union[str, UnsetType] = unset, **kwargs):
        """
        Settings for updating the GitHub Costs integration account. Only the provided fields are changed.

        :param enterprise_name: Slug of the GitHub enterprise, as in ``https://github.com/enterprises/<enterprise-name>`` , or login of a GitHub organization, as in ``https://github.com/<organization-name>``. An enterprise covers every organization it owns. Connecting both an enterprise and one of its organizations counts that organization's costs twice. The token in ``authentication`` must match: classic for an enterprise, fine-grained for an organization.
        :type enterprise_name: str, optional

        :param tags: Comma-separated list of custom tags for this GitHub Costs account.
        :type tags: str, optional
        """
        if enterprise_name is not unset:
            kwargs["enterprise_name"] = enterprise_name
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
