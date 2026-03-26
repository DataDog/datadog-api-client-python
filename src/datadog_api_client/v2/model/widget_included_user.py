# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.widget_included_user_attributes import WidgetIncludedUserAttributes


class WidgetIncludedUser(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.widget_included_user_attributes import WidgetIncludedUserAttributes

        return {
            "attributes": (WidgetIncludedUserAttributes,),
            "id": (str,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, id: str, type: str, attributes: Union[WidgetIncludedUserAttributes, UnsetType] = unset, **kwargs
    ):
        """
        A user resource included in the response.

        :param attributes: Attributes of an included user resource.
        :type attributes: WidgetIncludedUserAttributes, optional

        :param id: The unique identifier of the user.
        :type id: str

        :param type: Users resource type.
        :type type: str
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
