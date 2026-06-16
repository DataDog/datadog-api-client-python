# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.shared_dashboard_viewing_preferences_theme import (
        SharedDashboardViewingPreferencesTheme,
    )


class SharedDashboardViewingPreferences(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.shared_dashboard_viewing_preferences_theme import (
            SharedDashboardViewingPreferencesTheme,
        )

        return {
            "high_density": (bool,),
            "theme": (SharedDashboardViewingPreferencesTheme,),
        }

    attribute_map = {
        "high_density": "high_density",
        "theme": "theme",
    }

    def __init__(self_, high_density: bool, theme: SharedDashboardViewingPreferencesTheme, **kwargs):
        """
        Display settings for the shared dashboard.

        :param high_density: Whether widgets are displayed in high-density mode.
        :type high_density: bool

        :param theme: The theme of the shared dashboard view. ``system`` follows the viewer's system default.
        :type theme: SharedDashboardViewingPreferencesTheme
        """
        super().__init__(kwargs)

        self_.high_density = high_density
        self_.theme = theme
