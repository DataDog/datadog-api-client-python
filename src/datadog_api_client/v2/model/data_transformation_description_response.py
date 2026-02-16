# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DataTransformationDescriptionResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "details": (str,),
            "id": (str,),
            "summary": (str,),
        }

    attribute_map = {
        "details": "details",
        "id": "id",
        "summary": "summary",
    }

    def __init__(self_, details: str, id: str, summary: str, **kwargs):
        """


        :param details: Detailed description of the transformation.
        :type details: str

        :param id: The generation ID.
        :type id: str

        :param summary: A brief summary of the transformation.
        :type summary: str
        """
        super().__init__(kwargs)

        self_.details = details
        self_.id = id
        self_.summary = summary
