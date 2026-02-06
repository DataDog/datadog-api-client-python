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


class SetupRulesRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "disabled_default_rules": ([str],),
        }

    attribute_map = {
        "disabled_default_rules": "disabled_default_rules",
    }

    def __init__(self_, disabled_default_rules: Union[List[str], UnsetType] = unset, **kwargs):
        """
        Attributes for setting up rules.

        :param disabled_default_rules: Array of default rule IDs to disable.
        :type disabled_default_rules: [str], optional
        """
        if disabled_default_rules is not unset:
            kwargs["disabled_default_rules"] = disabled_default_rules
        super().__init__(kwargs)
