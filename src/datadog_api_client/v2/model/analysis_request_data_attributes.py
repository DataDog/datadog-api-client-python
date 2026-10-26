# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.analysis_request_options import AnalysisRequestOptions
    from datadog_api_client.v2.model.analysis_request_rule import AnalysisRequestRule


class AnalysisRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.analysis_request_options import AnalysisRequestOptions
        from datadog_api_client.v2.model.analysis_request_rule import AnalysisRequestRule

        return {
            "code": (str,),
            "file_encoding": (str,),
            "filename": (str,),
            "language": (str,),
            "options": (AnalysisRequestOptions,),
            "rules": ([AnalysisRequestRule],),
        }

    attribute_map = {
        "code": "code",
        "file_encoding": "file_encoding",
        "filename": "filename",
        "language": "language",
        "options": "options",
        "rules": "rules",
    }

    def __init__(
        self_,
        code: str,
        file_encoding: str,
        filename: str,
        language: str,
        rules: List[AnalysisRequestRule],
        options: Union[AnalysisRequestOptions, UnsetType] = unset,
        **kwargs,
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

        :param options: Analyzer options sent by browser-based clients. Accepted but ignored: the API always runs
            the analysis with tree-sitter enabled and rule output logged.
        :type options: AnalysisRequestOptions, optional

        :param rules: The list of static analysis rules to apply during analysis.
        :type rules: [AnalysisRequestRule]
        """
        if options is not unset:
            kwargs["options"] = options
        super().__init__(kwargs)

        self_.code = code
        self_.file_encoding = file_encoding
        self_.filename = filename
        self_.language = language
        self_.rules = rules
