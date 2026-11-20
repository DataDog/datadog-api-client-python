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
    from datadog_api_client.v1_20270101.model.context_menu_link_label import ContextMenuLinkLabel


class ContextMenuLink(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.context_menu_link_label import ContextMenuLinkLabel

        return {
            "is_hidden": (bool,),
            "link": (str,),
            "override_label": (ContextMenuLinkLabel,),
        }

    attribute_map = {
        "is_hidden": "is_hidden",
        "link": "link",
        "override_label": "override_label",
    }

    def __init__(
        self_,
        override_label: ContextMenuLinkLabel,
        is_hidden: Union[bool, UnsetType] = unset,
        link: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param is_hidden: Test-only generated schema for the dashboard versioning proof of concept.
        :type is_hidden: bool, optional

        :param link: Test-only generated schema for the dashboard versioning proof of concept.
        :type link: str, optional

        :param override_label: Test-only generated schema for the dashboard versioning proof of concept.
        :type override_label: ContextMenuLinkLabel
        """
        if is_hidden is not unset:
            kwargs["is_hidden"] = is_hidden
        if link is not unset:
            kwargs["link"] = link
        super().__init__(kwargs)

        self_.override_label = override_label
