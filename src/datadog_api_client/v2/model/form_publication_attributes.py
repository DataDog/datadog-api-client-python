# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class FormPublicationAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "version": (int,),
        }

    attribute_map = {
        "version": "version",
    }

    def __init__(self_, version: int, **kwargs):
        """


        :param version: The version number to publish.
        :type version: int
        """
        super().__init__(kwargs)

        self_.version = version
