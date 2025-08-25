# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.org_connection import OrgConnection


class OrgConnectionListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_connection import OrgConnection

        return {
            "data": ([OrgConnection],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[OrgConnection], **kwargs):
        """
        Response containing a list of org connections.

        :param data: List of org connections.
        :type data: [OrgConnection]
        """
        super().__init__(kwargs)

        self_.data = data
