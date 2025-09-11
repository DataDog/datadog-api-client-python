# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ItemApiPayloadMetaSchemaField(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "type": (str,),
        }

    attribute_map = {
        "name": "name",
        "type": "type",
    }

    def __init__(self_, name: str, type: str, **kwargs):
        """
        Information about a specific column in the datastore schema.

        :param name: The name of this column in the datastore.
        :type name: str

        :param type: The data type of this column. For example, 'string', 'number', or 'boolean'.
        :type type: str
        """
        super().__init__(kwargs)

        self_.name = name
        self_.type = type
