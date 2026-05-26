# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class GetAstRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "code": (str,),
            "file_encoding": (str,),
            "language": (str,),
        }

    attribute_map = {
        "code": "code",
        "file_encoding": "file_encoding",
        "language": "language",
    }

    def __init__(self_, code: str, file_encoding: str, language: str, **kwargs):
        """
        The attributes of the get-AST request, containing the source code to parse.

        :param code: The base64-encoded source code to parse into an abstract syntax tree.
        :type code: str

        :param file_encoding: The encoding of the source code file (must be utf-8).
        :type file_encoding: str

        :param language: The programming language of the source code to parse.
        :type language: str
        """
        super().__init__(kwargs)

        self_.code = code
        self_.file_encoding = file_encoding
        self_.language = language
