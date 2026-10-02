# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class TeamNotificationRuleAttributesServiceNow(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "templates": ([str],),
        }

    attribute_map = {
        "templates": "templates",
    }

    def __init__(self_, templates: Union[List[str], UnsetType] = unset, **kwargs):
        """
        ServiceNow notification settings for the team.

        :param templates: ServiceNow template handle names to use for notifications.
        :type templates: [str], optional
        """
        if templates is not unset:
            kwargs["templates"] = templates
        super().__init__(kwargs)
