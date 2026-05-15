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
    from datadog_api_client.v2.model.app_protection_level import AppProtectionLevel


class UpdateAppProtectionLevelRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.app_protection_level import AppProtectionLevel

        return {
            "protection_level": (AppProtectionLevel,),
        }

    attribute_map = {
        "protection_level": "protectionLevel",
    }

    def __init__(self_, protection_level: AppProtectionLevel, **kwargs):
        """
        Attributes for updating an app's publication protection level.

        :param protection_level: The publication protection level of the app. ``approval_required`` means changes must go through an approval workflow before being published.
        :type protection_level: AppProtectionLevel
        """
        super().__init__(kwargs)

        self_.protection_level = protection_level
