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
    from datadog_api_client.v2.model.app_builder_event_name import AppBuilderEventName
    from datadog_api_client.v2.model.app_builder_event_type import AppBuilderEventType


class AppBuilderEvent(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.app_builder_event_name import AppBuilderEventName
        from datadog_api_client.v2.model.app_builder_event_type import AppBuilderEventType

        return {
            "name": (AppBuilderEventName,),
            "type": (AppBuilderEventType,),
        }

    attribute_map = {
        "name": "name",
        "type": "type",
    }

    def __init__(
        self_,
        name: Union[AppBuilderEventName, UnsetType] = unset,
        type: Union[AppBuilderEventType, UnsetType] = unset,
        **kwargs,
    ):
        """
        An event on a UI component that triggers a response or action in an app.

        :param name: The triggering action for the event.
        :type name: AppBuilderEventName, optional

        :param type: The response to the event.
        :type type: AppBuilderEventType, optional
        """
        if name is not unset:
            kwargs["name"] = name
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
