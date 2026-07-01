# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CreateSnapshotTemplateVariable(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "prefix": (str,),
            "values": ([str],),
        }

    attribute_map = {
        "name": "name",
        "prefix": "prefix",
        "values": "values",
    }

    def __init__(self_, name: str, prefix: str, values: List[str], **kwargs):
        """
        A template variable definition for snapshot rendering.

        :param name: The template variable name.
        :type name: str

        :param prefix: The tag prefix associated with the template variable. For example, a prefix of ``host`` with a value of ``web-server-1`` scopes the snapshot to ``host:web-server-1``.
        :type prefix: str

        :param values: The list of scoped values for this template variable.
        :type values: [str]
        """
        super().__init__(kwargs)

        self_.name = name
        self_.prefix = prefix
        self_.values = values
