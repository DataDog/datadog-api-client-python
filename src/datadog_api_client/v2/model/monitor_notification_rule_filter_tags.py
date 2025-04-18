# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MonitorNotificationRuleFilterTags(ModelNormal):
    validations = {
        "tags": {
            "max_items": 20,
            "min_items": 1,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "tags": ([str],),
        }

    attribute_map = {
        "tags": "tags",
    }

    def __init__(self_, tags: List[str], **kwargs):
        """
        Filter monitors by tags. Monitors must match all tags.

        :param tags: A list of monitor tags.
        :type tags: [str]
        """
        super().__init__(kwargs)

        self_.tags = tags
