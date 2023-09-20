# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.tags_event_attribute import TagsEventAttribute
    from datadog_api_client.v2.model.ci_app_test_level import CIAppTestLevel


class CIAppEventAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tags_event_attribute import TagsEventAttribute
        from datadog_api_client.v2.model.ci_app_test_level import CIAppTestLevel

        return {
            "attributes": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "tags": (TagsEventAttribute,),
            "test_level": (CIAppTestLevel,),
        }

    attribute_map = {
        "attributes": "attributes",
        "tags": "tags",
        "test_level": "test_level",
    }

    def __init__(
        self_,
        attributes: Union[Dict[str, Any], UnsetType] = unset,
        tags: Union[TagsEventAttribute, UnsetType] = unset,
        test_level: Union[CIAppTestLevel, UnsetType] = unset,
        **kwargs,
    ):
        """
        JSON object containing all event attributes and their associated values.

        :param attributes: JSON object of attributes from CI Visibility test events.
        :type attributes: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param tags: Array of tags associated with your event.
        :type tags: TagsEventAttribute, optional

        :param test_level: Test run level.
        :type test_level: CIAppTestLevel, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if tags is not unset:
            kwargs["tags"] = tags
        if test_level is not unset:
            kwargs["test_level"] = test_level
        super().__init__(kwargs)
