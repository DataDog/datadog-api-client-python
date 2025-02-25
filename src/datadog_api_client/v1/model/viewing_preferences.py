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
    from datadog_api_client.v1.model.viewing_preferences_theme import ViewingPreferencesTheme


class ViewingPreferences(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.viewing_preferences_theme import ViewingPreferencesTheme

        return {
            "high_density": (bool,),
            "theme": (ViewingPreferencesTheme,),
        }

    attribute_map = {
        "high_density": "high_density",
        "theme": "theme",
    }

    def __init__(
        self_,
        high_density: Union[bool, UnsetType] = unset,
        theme: Union[ViewingPreferencesTheme, UnsetType] = unset,
        **kwargs,
    ):
        """
        The viewing preferences for a shared dashboard.

        :param high_density: Whether the widgets on the shared dashboard should be displayed with high density.
        :type high_density: bool, optional

        :param theme: The theme of the shared dashboard view. "system" follows your system's default viewing theme.
        :type theme: ViewingPreferencesTheme, optional
        """
        if high_density is not unset:
            kwargs["high_density"] = high_density
        if theme is not unset:
            kwargs["theme"] = theme
        super().__init__(kwargs)
