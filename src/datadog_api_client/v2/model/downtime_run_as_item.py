# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DowntimeRunAsItem(ModelNormal):
    validations = {
        "principals": {
            "max_items": 1,
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "principals": ([str],),
        }

    attribute_map = {
        "principals": "principals",
    }

    def __init__(self_, principals: List[str], **kwargs):
        """
        A set of principals the downtime runs as.

        :param principals: The principal the downtime runs as. Only one user is supported.
        :type principals: [str]
        """
        super().__init__(kwargs)

        self_.principals = principals
