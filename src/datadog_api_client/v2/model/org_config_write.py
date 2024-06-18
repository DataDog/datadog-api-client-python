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
    from datadog_api_client.v2.model.org_config_write_attributes import OrgConfigWriteAttributes
    from datadog_api_client.v2.model.org_config_type import OrgConfigType


class OrgConfigWrite(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_config_write_attributes import OrgConfigWriteAttributes
        from datadog_api_client.v2.model.org_config_type import OrgConfigType

        return {
            "attributes": (OrgConfigWriteAttributes,),
            "type": (OrgConfigType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: OrgConfigWriteAttributes, type: OrgConfigType, **kwargs):
        """
        An Org Config write operation.

        :param attributes: Writable attributes of an Org Config.
        :type attributes: OrgConfigWriteAttributes

        :param type: Data type of an Org Config.
        :type type: OrgConfigType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
