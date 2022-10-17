# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.tags_event_attribute import TagsEventAttribute
from datadog_api_client.v2.model.ci_app_event_attributes import CIAppEventAttributes
from datadog_api_client.v2.model.tags_event_attribute import TagsEventAttribute

if TYPE_CHECKING:
    from datadog_api_client.v2.model.ci_app_test_event_type_name import CIAppTestEventTypeName


@dataclass
class CIAppTestEventJSON:
    id: str
    attributes: Union[Dict[str, Any], UnsetType] = unset
    service: Union[str, UnsetType] = unset
    tags: Union[TagsEventAttribute, UnsetType] = unset
    timestamp: Union[datetime, UnsetType] = unset


class CIAppTestEvent(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ci_app_test_event_type_name import CIAppTestEventTypeName

        return {
            "attributes": (CIAppEventAttributes,),
            "id": (str,),
            "type": (CIAppTestEventTypeName,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    json_api_model = CIAppTestEventJSON

    def __init__(
        self_,
        attributes: Union[CIAppEventAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[CIAppTestEventTypeName, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object description of test event after being processed and stored by Datadog.

        :param attributes: JSON object containing all event attributes and their associated values.
        :type attributes: CIAppEventAttributes, optional

        :param id: Unique ID of the event.
        :type id: str, optional

        :param type: Type of the event.
        :type type: CIAppTestEventTypeName, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
