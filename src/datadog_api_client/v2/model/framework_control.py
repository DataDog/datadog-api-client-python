# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class FrameworkControl(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "rule_ids": ([str],),
        }

    attribute_map = {
        "name": "name",
        "rule_ids": "rule_ids",
    }

    def __init__(self_, name: str, rule_ids: List[str], **kwargs):
        """
        Framework Control.

        :param name: Control Name.
        :type name: str

        :param rule_ids: Rule IDs.
        :type rule_ids: [str]
        """
        super().__init__(kwargs)

        self_.name = name
        self_.rule_ids = rule_ids
