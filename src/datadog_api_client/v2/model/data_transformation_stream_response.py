# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DataTransformationStreamResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "content": (str,),
            "id": (str,),
        }

    attribute_map = {
        "content": "content",
        "id": "id",
    }

    def __init__(self_, content: str, id: str, **kwargs):
        """


        :param content: The generated code or explanation chunk.
        :type content: str

        :param id: The generation ID.
        :type id: str
        """
        super().__init__(kwargs)

        self_.content = content
        self_.id = id
