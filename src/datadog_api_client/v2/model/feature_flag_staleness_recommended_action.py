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


class FeatureFlagStalenessRecommendedAction(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "action": (str,),
            "description": (str,),
        }

    attribute_map = {
        "action": "action",
        "description": "description",
    }

    def __init__(self_, action: Union[str, UnsetType] = unset, description: Union[str, UnsetType] = unset, **kwargs):
        """
        An action suggested for a feature flag based on its staleness state.

        :param action: The action to consider. Values include ``remove_from_code`` , ``archive_flag`` , ``mark_as_permanent`` , ``snooze`` , and ``check_sdk_config``.
        :type action: str, optional

        :param description: An explanation of the suggested action.
        :type description: str, optional
        """
        if action is not unset:
            kwargs["action"] = action
        if description is not unset:
            kwargs["description"] = description
        super().__init__(kwargs)
