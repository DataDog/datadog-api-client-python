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
    from datadog_api_client.v2.model.on_call_page_link_attributes import OnCallPageLinkAttributes
    from datadog_api_client.v2.model.on_call_page_link_type import OnCallPageLinkType


class OnCallPageLink(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_page_link_attributes import OnCallPageLinkAttributes
        from datadog_api_client.v2.model.on_call_page_link_type import OnCallPageLinkType

        return {
            "attributes": (OnCallPageLinkAttributes,),
            "id": (str,),
            "type": (OnCallPageLinkType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: OnCallPageLinkType,
        attributes: Union[OnCallPageLinkAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        A link between a page and another Datadog resource, such as an incident.

        :param attributes: The attributes of a page link. A page can be the child of another Datadog resource
            (for example, when an incident triggers it), or the parent of one (for example, when the
            page is escalated to an incident).
        :type attributes: OnCallPageLinkAttributes, optional

        :param id: The ID of the link.
        :type id: str

        :param type: Page link resource type.
        :type type: OnCallPageLinkType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
