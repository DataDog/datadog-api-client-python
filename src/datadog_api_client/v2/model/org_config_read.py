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
    from datadog_api_client.v2.model.org_config_read_attributes import OrgConfigReadAttributes
    from datadog_api_client.v2.model.org_config_type import OrgConfigType


class OrgConfigRead(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_config_read_attributes import OrgConfigReadAttributes
        from datadog_api_client.v2.model.org_config_type import OrgConfigType

        return {
            "attributes": (OrgConfigReadAttributes,),
            "id": (str,),
            "type": (OrgConfigType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: OrgConfigReadAttributes, id: str, type: OrgConfigType, **kwargs):
        """
        A single Org Config.

        :param attributes: Readable attributes of an Org Config.
        :type attributes: OrgConfigReadAttributes

        :param id: A unique identifier for an Org Config.
        :type id: str

        :param type: Data type of an Org Config.
        :type type: OrgConfigType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
