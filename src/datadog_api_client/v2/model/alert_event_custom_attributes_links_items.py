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
    from datadog_api_client.v2.model.alert_event_custom_attributes_links_items_category import (
        AlertEventCustomAttributesLinksItemsCategory,
    )


class AlertEventCustomAttributesLinksItems(ModelNormal):
    validations = {
        "title": {
            "max_length": 300,
            "min_length": 1,
        },
        "url": {
            "max_length": 2048,
            "min_length": 1,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.alert_event_custom_attributes_links_items_category import (
            AlertEventCustomAttributesLinksItemsCategory,
        )

        return {
            "category": (AlertEventCustomAttributesLinksItemsCategory,),
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
        category: AlertEventCustomAttributesLinksItemsCategory,
        url: str,
        title: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A link.

        :param category: The category of the link.
        :type category: AlertEventCustomAttributesLinksItemsCategory

        :param title: The display text of the link. Limited to 300 characters.
        :type title: str, optional

        :param url: The URL of the link. Limited to 2048 characters.
        :type url: str
        """
        if title is not unset:
            kwargs["title"] = title
        super().__init__(kwargs)

        self_.category = category
        self_.url = url
