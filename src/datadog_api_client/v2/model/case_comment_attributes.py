# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CaseCommentAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "comment": (str,),
        }

    attribute_map = {
        "comment": "comment",
    }

    def __init__(self_, comment: str, **kwargs):
        """
        Case comment attributes

        :param comment: The ``CaseCommentAttributes`` ``message``.
        :type comment: str
        """
        super().__init__(kwargs)

        self_.comment = comment
