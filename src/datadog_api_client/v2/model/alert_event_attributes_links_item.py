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
    from datadog_api_client.v2.model.alert_event_attributes_links_item_category import (
        AlertEventAttributesLinksItemCategory,
    )


class AlertEventAttributesLinksItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.alert_event_attributes_links_item_category import (
            AlertEventAttributesLinksItemCategory,
        )

        return {
            "category": (AlertEventAttributesLinksItemCategory,),
            "title": (str,),
            "url": (str,),
        }

    attribute_map = {
        "category": "category",
        "title": "title",
        "url": "url",
    }

    def __init__(
        self_,
        category: Union[AlertEventAttributesLinksItemCategory, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        url: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A link.

        :param category: The category of the link.
        :type category: AlertEventAttributesLinksItemCategory, optional

        :param title: The display text of the link.
        :type title: str, optional

        :param url: The URL of the link.
        :type url: str, optional
        """
        if category is not unset:
            kwargs["category"] = category
        if title is not unset:
            kwargs["title"] = title
        if url is not unset:
            kwargs["url"] = url
        super().__init__(kwargs)
