# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.secure_embed_global_time import SecureEmbedGlobalTime
    from datadog_api_client.v2.model.secure_embed_selectable_template_variable import (
        SecureEmbedSelectableTemplateVariable,
    )
    from datadog_api_client.v2.model.secure_embed_status import SecureEmbedStatus
    from datadog_api_client.v2.model.secure_embed_viewing_preferences import SecureEmbedViewingPreferences


class SecureEmbedUpdateRequestAttributes(ModelNormal):
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
        global_time: Union[SecureEmbedGlobalTime, UnsetType] = unset,
        global_time_selectable: Union[bool, UnsetType] = unset,
        selectable_template_vars: Union[List[SecureEmbedSelectableTemplateVariable], UnsetType] = unset,
        status: Union[SecureEmbedStatus, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        viewing_preferences: Union[SecureEmbedViewingPreferences, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for updating a secure embed shared dashboard. All fields are optional.

        :param global_time: Default time range configuration for the secure embed.
        :type global_time: SecureEmbedGlobalTime, optional

        :param global_time_selectable: Updated time selectability.
        :type global_time_selectable: bool, optional

        :param selectable_template_vars: Updated template variables.
        :type selectable_template_vars: [SecureEmbedSelectableTemplateVariable], optional

        :param status: The status of the secure embed share. Active means the shared dashboard is available. Paused means it is not.
        :type status: SecureEmbedStatus, optional

        :param title: Updated title.
        :type title: str, optional

        :param viewing_preferences: Display settings for the secure embed shared dashboard.
        :type viewing_preferences: SecureEmbedViewingPreferences, optional
        """
        if global_time is not unset:
            kwargs["global_time"] = global_time
        if global_time_selectable is not unset:
            kwargs["global_time_selectable"] = global_time_selectable
        if selectable_template_vars is not unset:
            kwargs["selectable_template_vars"] = selectable_template_vars
        if status is not unset:
            kwargs["status"] = status
        if title is not unset:
            kwargs["title"] = title
        if viewing_preferences is not unset:
            kwargs["viewing_preferences"] = viewing_preferences
        super().__init__(kwargs)
