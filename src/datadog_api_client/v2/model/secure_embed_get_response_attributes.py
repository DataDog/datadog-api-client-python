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
    from datadog_api_client.v2.model.secure_embed_share_type import SecureEmbedShareType
    from datadog_api_client.v2.model.secure_embed_status import SecureEmbedStatus
    from datadog_api_client.v2.model.secure_embed_viewing_preferences import SecureEmbedViewingPreferences


class SecureEmbedGetResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.secure_embed_global_time import SecureEmbedGlobalTime
        from datadog_api_client.v2.model.secure_embed_selectable_template_variable import (
            SecureEmbedSelectableTemplateVariable,
        )
        from datadog_api_client.v2.model.secure_embed_share_type import SecureEmbedShareType
        from datadog_api_client.v2.model.secure_embed_status import SecureEmbedStatus
        from datadog_api_client.v2.model.secure_embed_viewing_preferences import SecureEmbedViewingPreferences

        return {
            "created_at": (str,),
            "credential_suffix": (str,),
            "dashboard_id": (str,),
            "global_time": (SecureEmbedGlobalTime,),
            "global_time_selectable": (bool,),
            "id": (str,),
            "selectable_template_vars": ([SecureEmbedSelectableTemplateVariable],),
            "share_type": (SecureEmbedShareType,),
            "status": (SecureEmbedStatus,),
            "title": (str,),
            "token": (str,),
            "url": (str,),
            "viewing_preferences": (SecureEmbedViewingPreferences,),
        }

    attribute_map = {
        "created_at": "created_at",
        "credential_suffix": "credential_suffix",
        "dashboard_id": "dashboard_id",
        "global_time": "global_time",
        "global_time_selectable": "global_time_selectable",
        "id": "id",
        "selectable_template_vars": "selectable_template_vars",
        "share_type": "share_type",
        "status": "status",
        "title": "title",
        "token": "token",
        "url": "url",
        "viewing_preferences": "viewing_preferences",
    }
    read_only_vars = {
        "created_at",
        "credential_suffix",
        "dashboard_id",
        "id",
        "token",
        "url",
    }

    def __init__(
        self_,
        created_at: Union[str, UnsetType] = unset,
        credential_suffix: Union[str, UnsetType] = unset,
        dashboard_id: Union[str, UnsetType] = unset,
        global_time: Union[SecureEmbedGlobalTime, UnsetType] = unset,
        global_time_selectable: Union[bool, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        selectable_template_vars: Union[List[SecureEmbedSelectableTemplateVariable], UnsetType] = unset,
        share_type: Union[SecureEmbedShareType, UnsetType] = unset,
        status: Union[SecureEmbedStatus, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        token: Union[str, UnsetType] = unset,
        url: Union[str, UnsetType] = unset,
        viewing_preferences: Union[SecureEmbedViewingPreferences, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an existing secure embed shared dashboard.

        :param created_at: Creation timestamp.
        :type created_at: str, optional

        :param credential_suffix: Last 4 characters of the credential. Defaults to ``0000`` if unavailable.
        :type credential_suffix: str, optional

        :param dashboard_id: The source dashboard ID.
        :type dashboard_id: str, optional

        :param global_time: Default time range configuration for the secure embed.
        :type global_time: SecureEmbedGlobalTime, optional

        :param global_time_selectable: Whether time range is viewer-selectable.
        :type global_time_selectable: bool, optional

        :param id: Internal share ID.
        :type id: str, optional

        :param selectable_template_vars: Template variables with their configuration.
        :type selectable_template_vars: [SecureEmbedSelectableTemplateVariable], optional

        :param share_type: The type of share. Always ``secure_embed``.
        :type share_type: SecureEmbedShareType, optional

        :param status: The status of the secure embed share. Active means the shared dashboard is available. Paused means it is not.
        :type status: SecureEmbedStatus, optional

        :param title: Display title.
        :type title: str, optional

        :param token: Public share token.
        :type token: str, optional

        :param url: CDN URL for the shared dashboard.
        :type url: str, optional

        :param viewing_preferences: Display settings for the secure embed shared dashboard.
        :type viewing_preferences: SecureEmbedViewingPreferences, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if credential_suffix is not unset:
            kwargs["credential_suffix"] = credential_suffix
        if dashboard_id is not unset:
            kwargs["dashboard_id"] = dashboard_id
        if global_time is not unset:
            kwargs["global_time"] = global_time
        if global_time_selectable is not unset:
            kwargs["global_time_selectable"] = global_time_selectable
        if id is not unset:
            kwargs["id"] = id
        if selectable_template_vars is not unset:
            kwargs["selectable_template_vars"] = selectable_template_vars
        if share_type is not unset:
            kwargs["share_type"] = share_type
        if status is not unset:
            kwargs["status"] = status
        if title is not unset:
            kwargs["title"] = title
        if token is not unset:
            kwargs["token"] = token
        if url is not unset:
            kwargs["url"] = url
        if viewing_preferences is not unset:
            kwargs["viewing_preferences"] = viewing_preferences
        super().__init__(kwargs)
