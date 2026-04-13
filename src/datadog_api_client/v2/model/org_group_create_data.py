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
    from datadog_api_client.v2.model.org_group_create_attributes import OrgGroupCreateAttributes
    from datadog_api_client.v2.model.org_group_type import OrgGroupType


class OrgGroupCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_create_attributes import OrgGroupCreateAttributes
        from datadog_api_client.v2.model.org_group_type import OrgGroupType

        return {
            "attributes": (OrgGroupCreateAttributes,),
            "type": (OrgGroupType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: OrgGroupCreateAttributes, type: OrgGroupType, **kwargs):
        """
        Data for creating an org group.

        :param attributes: Attributes for creating an org group.
        :type attributes: OrgGroupCreateAttributes

        :param type: Org groups resource type.
        :type type: OrgGroupType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
