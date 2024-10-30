# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class DomainAllowlistAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "domains": ([str],),
            "enabled": (bool,),
        }

    attribute_map = {
        "domains": "domains",
        "enabled": "enabled",
    }

    def __init__(
        self_, domains: Union[List[str], UnsetType] = unset, enabled: Union[bool, UnsetType] = unset, **kwargs
    ):
        """
        The details of the email domain allowlist.

        :param domains: The list of domains in the email domain allowlist.
        :type domains: [str], optional

        :param enabled: Whether the email domain allowlist is enabled for the org.
        :type enabled: bool, optional
        """
        if domains is not unset:
            kwargs["domains"] = domains
        if enabled is not unset:
            kwargs["enabled"] = enabled
        super().__init__(kwargs)
