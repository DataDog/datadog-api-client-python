# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RulesetRespDataAttributesRulesItemsMapping(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "destination_key": (str,),
            "if_not_exists": (bool,),
            "source_keys": ([str],),
        }

    attribute_map = {
        "destination_key": "destination_key",
        "if_not_exists": "if_not_exists",
        "source_keys": "source_keys",
    }

    def __init__(self_, destination_key: str, if_not_exists: bool, source_keys: List[str], **kwargs):
        """
        The definition of ``RulesetRespDataAttributesRulesItemsMapping`` object.

        :param destination_key: The ``mapping`` ``destination_key``.
        :type destination_key: str

        :param if_not_exists: The ``mapping`` ``if_not_exists``.
        :type if_not_exists: bool

        :param source_keys: The ``mapping`` ``source_keys``.
        :type source_keys: [str]
        """
        super().__init__(kwargs)

        self_.destination_key = destination_key
        self_.if_not_exists = if_not_exists
        self_.source_keys = source_keys
