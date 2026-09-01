# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LLMObsFrontendContent(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "code": (str,),
        }

    attribute_map = {
        "code": "code",
    }

    def __init__(self_, code: str, **kwargs):
        """
        Web content that makes up a ``frontend`` interaction.

        :param code: Caller-provided web content.
        :type code: str
        """
        super().__init__(kwargs)

        self_.code = code
