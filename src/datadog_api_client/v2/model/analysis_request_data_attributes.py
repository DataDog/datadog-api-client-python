# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.analysis_request_rule import AnalysisRequestRule


class AnalysisRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.analysis_request_rule import AnalysisRequestRule

        return {
            "code": (str,),
            "file_encoding": (str,),
            "filename": (str,),
            "language": (str,),
            "rules": ([AnalysisRequestRule],),
        }

    attribute_map = {
        "code": "code",
        "file_encoding": "file_encoding",
        "filename": "filename",
        "language": "language",
        "rules": "rules",
    }

    def __init__(
        self_, code: str, file_encoding: str, filename: str, language: str, rules: List[AnalysisRequestRule], **kwargs
    ):
        """
        The attributes of the analysis request, containing the source code and rules to apply.

        :param code: The base64-encoded source code to analyze.
        :type code: str

        :param file_encoding: The encoding of the source code file (must be ``utf-8`` ).
        :type file_encoding: str

        :param filename: The name of the file being analyzed.
        :type filename: str

        :param language: The programming language of the source code.
        :type language: str

        :param rules: The list of static analysis rules to apply during analysis.
        :type rules: [AnalysisRequestRule]
        """
        super().__init__(kwargs)

        self_.code = code
        self_.file_encoding = file_encoding
        self_.filename = filename
        self_.language = language
        self_.rules = rules
