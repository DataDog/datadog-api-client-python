# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CustomFrameworkControl(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "rules_id": ([str],),
        }

    attribute_map = {
        "name": "name",
        "rules_id": "rules_id",
    }

    def __init__(self_, name: str, rules_id: List[str], **kwargs):
        """
        Framework Control.

        :param name: Control Name.
        :type name: str

        :param rules_id: Rule IDs.
        :type rules_id: [str]
        """
        super().__init__(kwargs)

        self_.name = name
        self_.rules_id = rules_id
