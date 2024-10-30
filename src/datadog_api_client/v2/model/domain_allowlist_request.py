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
    from datadog_api_client.v2.model.domain_allowlist import DomainAllowlist


class DomainAllowlistRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.domain_allowlist import DomainAllowlist

        return {
            "data": (DomainAllowlist,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: DomainAllowlist, **kwargs):
        """
        Request containing the desired email domain allowlist configuration.

        :param data: The email domain allowlist for an org.
        :type data: DomainAllowlist
        """
        super().__init__(kwargs)

        self_.data = data
