# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.secure_embed_global_time import SecureEmbedGlobalTime
    from datadog_api_client.v2.model.secure_embed_selectable_template_variable import (
        SecureEmbedSelectableTemplateVariable,
    )
    from datadog_api_client.v2.model.secure_embed_status import SecureEmbedStatus
    from datadog_api_client.v2.model.secure_embed_viewing_preferences import SecureEmbedViewingPreferences


class SecureEmbedCreateRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.secure_embed_global_time import SecureEmbedGlobalTime
        from datadog_api_client.v2.model.secure_embed_selectable_template_variable import (
            SecureEmbedSelectableTemplateVariable,
        )
        from datadog_api_client.v2.model.secure_embed_status import SecureEmbedStatus
        from datadog_api_client.v2.model.secure_embed_viewing_preferences import SecureEmbedViewingPreferences

        return {
            "global_time": (SecureEmbedGlobalTime,),
            "global_time_selectable": (bool,),
            "selectable_template_vars": ([SecureEmbedSelectableTemplateVariable],),
            "status": (SecureEmbedStatus,),
            "title": (str,),
            "viewing_preferences": (SecureEmbedViewingPreferences,),
        }

    attribute_map = {
        "global_time": "global_time",
        "global_time_selectable": "global_time_selectable",
        "selectable_template_vars": "selectable_template_vars",
        "status": "status",
        "title": "title",
        "viewing_preferences": "viewing_preferences",
    }

    def __init__(
        self_,
        global_time: SecureEmbedGlobalTime,
        global_time_selectable: bool,
        selectable_template_vars: List[SecureEmbedSelectableTemplateVariable],
        status: SecureEmbedStatus,
        title: str,
        viewing_preferences: SecureEmbedViewingPreferences,
        **kwargs,
    ):
        """
        Attributes for creating a secure embed shared dashboard.

        :param global_time: Default time range configuration for the secure embed.
        :type global_time: SecureEmbedGlobalTime

        :param global_time_selectable: Whether viewers can change the time range.
        :type global_time_selectable: bool

        :param selectable_template_vars: Template variables viewers can modify.
        :type selectable_template_vars: [SecureEmbedSelectableTemplateVariable]

        :param status: The status of the secure embed share. Active means the shared dashboard is available. Paused means it is not.
        :type status: SecureEmbedStatus

        :param title: Display title for the shared dashboard.
        :type title: str

        :param viewing_preferences: Display settings for the secure embed shared dashboard.
        :type viewing_preferences: SecureEmbedViewingPreferences
        """
        super().__init__(kwargs)

        self_.global_time = global_time
        self_.global_time_selectable = global_time_selectable
        self_.selectable_template_vars = selectable_template_vars
        self_.status = status
        self_.title = title
        self_.viewing_preferences = viewing_preferences
