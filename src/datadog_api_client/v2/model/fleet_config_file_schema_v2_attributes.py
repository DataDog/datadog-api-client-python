# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class FleetConfigFileSchemaV2Attributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "schema": (dict,),
        }

    attribute_map = {
        "schema": "schema",
    }

    def __init__(self_, schema: dict, **kwargs):
        """
        Attributes for a configuration file's schema.

        :param schema: The schema for the requested configuration file.
        :type schema: dict
        """
        super().__init__(kwargs)

        self_.schema = schema
