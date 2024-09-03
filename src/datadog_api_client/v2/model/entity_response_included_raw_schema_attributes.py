# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class EntityResponseIncludedRawSchemaAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "raw_schema": (str,),
        }

    attribute_map = {
        "raw_schema": "rawSchema",
    }

    def __init__(self_, raw_schema: Union[str, UnsetType] = unset, **kwargs):
        """
        Included raw schema attributes.

        :param raw_schema: Schema from user input in base64 encoding.
        :type raw_schema: str, optional
        """
        if raw_schema is not unset:
            kwargs["raw_schema"] = raw_schema
        super().__init__(kwargs)
