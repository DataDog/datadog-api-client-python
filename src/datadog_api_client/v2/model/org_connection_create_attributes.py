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
    from datadog_api_client.v2.model.org_connection_type_enum import OrgConnectionTypeEnum


class OrgConnectionCreateAttributes(ModelNormal):
    validations = {
        "connection_types": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_connection_type_enum import OrgConnectionTypeEnum

        return {
            "connection_types": ([OrgConnectionTypeEnum],),
        }

    attribute_map = {
        "connection_types": "connection_types",
    }

    def __init__(self_, connection_types: List[OrgConnectionTypeEnum], **kwargs):
        """
        Attributes for creating an org connection.

        :param connection_types: List of connection types to establish.
        :type connection_types: [OrgConnectionTypeEnum]
        """
        super().__init__(kwargs)

        self_.connection_types = connection_types
