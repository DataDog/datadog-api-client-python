# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ProjectCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "key": (str,),
            "name": (str,),
        }

    attribute_map = {
        "key": "key",
        "name": "name",
    }

    def __init__(self_, key: str, name: str, **kwargs):
        """
        Project creation attributes

        :param key: Project's key. Cannot be "CASE"
        :type key: str

        :param name: name
        :type name: str
        """
        super().__init__(kwargs)

        self_.key = key
        self_.name = name
