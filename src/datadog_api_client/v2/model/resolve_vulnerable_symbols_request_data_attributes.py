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


class ResolveVulnerableSymbolsRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "purls": ([str],),
        }

    attribute_map = {
        "purls": "purls",
    }

    def __init__(self_, purls: Union[List[str], UnsetType] = unset, **kwargs):
        """


        :param purls:
        :type purls: [str], optional
        """
        if purls is not unset:
            kwargs["purls"] = purls
        super().__init__(kwargs)
