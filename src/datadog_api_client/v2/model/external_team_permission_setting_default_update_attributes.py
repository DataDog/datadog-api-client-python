# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ExternalTeamPermissionSettingDefaultUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }

    attribute_map = {
        "value": "value",
    }

    def __init__(self_, value: str, **kwargs):
        """
        Attributes for upserting an external team permission setting default.

        :param value: The default permission value to apply for the action.
        :type value: str
        """
        super().__init__(kwargs)

        self_.value = value
