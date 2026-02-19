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
    from datadog_api_client.v2.model.change_request_included_user_attributes import ChangeRequestIncludedUserAttributes


class ChangeRequestIncludedUser(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.change_request_included_user_attributes import (
            ChangeRequestIncludedUserAttributes,
        )

        return {
            "attributes": (ChangeRequestIncludedUserAttributes,),
            "id": (str,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: ChangeRequestIncludedUserAttributes, id: str, type: str, **kwargs):
        """
        An included user resource.

        :param attributes: Attributes of an included user.
        :type attributes: ChangeRequestIncludedUserAttributes

        :param id: The user UUID.
        :type id: str

        :param type: The resource type.
        :type type: str
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
