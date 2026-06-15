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
    from datadog_api_client.v2.model.global_org_attributes import GlobalOrgAttributes
    from datadog_api_client.v2.model.global_org_type import GlobalOrgType


class GlobalOrgData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.global_org_attributes import GlobalOrgAttributes
        from datadog_api_client.v2.model.global_org_type import GlobalOrgType

        return {
            "attributes": (GlobalOrgAttributes,),
            "type": (GlobalOrgType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: GlobalOrgAttributes, type: GlobalOrgType, **kwargs):
        """
        An organization associated with the authenticated user.

        :param attributes: Attributes of an organization associated with the authenticated user.
        :type attributes: GlobalOrgAttributes

        :param type: The resource type for global user organizations.
        :type type: GlobalOrgType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
