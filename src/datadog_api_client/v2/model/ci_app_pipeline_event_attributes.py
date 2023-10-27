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
    from datadog_api_client.v2.model.ci_app_pipeline_level import CIAppPipelineLevel
    from datadog_api_client.v2.model.tags_event_attribute import TagsEventAttribute


class CIAppPipelineEventAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ci_app_pipeline_level import CIAppPipelineLevel
        from datadog_api_client.v2.model.tags_event_attribute import TagsEventAttribute

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
            "ci_level": (CIAppPipelineLevel,),
            "tags": (TagsEventAttribute,),
        }

    attribute_map = {
        "attributes": "attributes",
        "ci_level": "ci_level",
        "tags": "tags",
    }

    def __init__(
        self_,
        attributes: Union[Dict[str, Any], UnsetType] = unset,
        ci_level: Union[CIAppPipelineLevel, UnsetType] = unset,
        tags: Union[TagsEventAttribute, UnsetType] = unset,
        **kwargs,
    ):
        """
        JSON object containing all event attributes and their associated values.

        :param attributes: JSON object of attributes from CI Visibility pipeline events.
        :type attributes: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param ci_level: Pipeline execution level.
        :type ci_level: CIAppPipelineLevel, optional

        :param tags: Array of tags associated with your event.
        :type tags: TagsEventAttribute, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if ci_level is not unset:
            kwargs["ci_level"] = ci_level
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
