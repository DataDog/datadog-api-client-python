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
    from datadog_api_client.v2.model.saved_filter_environment_reference import SavedFilterEnvironmentReference
    from datadog_api_client.v2.model.saved_filter_flag_reference import SavedFilterFlagReference


class SavedFilterPermissionDeniedAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.saved_filter_environment_reference import SavedFilterEnvironmentReference
        from datadog_api_client.v2.model.saved_filter_flag_reference import SavedFilterFlagReference

        return {
            "denied_environments": ([SavedFilterEnvironmentReference],),
            "denied_flags": ([SavedFilterFlagReference],),
            "message": (str,),
        }

    attribute_map = {
        "denied_environments": "denied_environments",
        "denied_flags": "denied_flags",
        "message": "message",
    }

    def __init__(
        self_,
        denied_flags: List[SavedFilterFlagReference],
        message: str,
        denied_environments: Union[List[SavedFilterEnvironmentReference], UnsetType] = unset,
        **kwargs,
    ):
        """
        The caller lacks edit permission on one or more feature flags that reference this saved filter, or on one or more of their environments.

        :param denied_environments: Environments preventing this update.
        :type denied_environments: [SavedFilterEnvironmentReference], optional

        :param denied_flags: Feature flags preventing this update.
        :type denied_flags: [SavedFilterFlagReference]

        :param message: The reason the saved filter update was rejected.
        :type message: str
        """
        if denied_environments is not unset:
            kwargs["denied_environments"] = denied_environments
        super().__init__(kwargs)

        self_.denied_flags = denied_flags
        self_.message = message
