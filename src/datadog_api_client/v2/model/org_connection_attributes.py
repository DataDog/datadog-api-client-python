# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.org_connection_type_enum import OrgConnectionTypeEnum


class OrgConnectionAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_connection_type_enum import OrgConnectionTypeEnum

        return {
            "connection_types": ([OrgConnectionTypeEnum],),
            "created_at": (datetime,),
        }

    attribute_map = {
        "connection_types": "connection_types",
        "created_at": "created_at",
    }

    def __init__(self_, connection_types: List[OrgConnectionTypeEnum], created_at: datetime, **kwargs):
        """
        Org connection attributes.

        :param connection_types: List of connection types.
        :type connection_types: [OrgConnectionTypeEnum]

        :param created_at: Timestamp when the connection was created.
        :type created_at: datetime
        """
        super().__init__(kwargs)

        self_.connection_types = connection_types
        self_.created_at = created_at
