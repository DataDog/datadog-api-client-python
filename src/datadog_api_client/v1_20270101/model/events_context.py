# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class EventsContext(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "context_event": (str,),
            "to_event": (str,),
        }

    attribute_map = {
        "context_event": "context_event",
        "to_event": "to_event",
    }

    def __init__(
        self_, context_event: Union[str, UnsetType] = unset, to_event: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param context_event: Test-only generated schema for the dashboard versioning proof of concept.
        :type context_event: str, optional

        :param to_event: Test-only generated schema for the dashboard versioning proof of concept.
        :type to_event: str, optional
        """
        if context_event is not unset:
            kwargs["context_event"] = context_event
        if to_event is not unset:
            kwargs["to_event"] = to_event
        super().__init__(kwargs)
