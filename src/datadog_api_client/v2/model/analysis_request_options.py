# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class AnalysisRequestOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "log_output": (bool,),
            "use_tree_sitter": (bool,),
        }

    attribute_map = {
        "log_output": "log_output",
        "use_tree_sitter": "use_tree_sitter",
    }

    def __init__(
        self_, log_output: Union[bool, UnsetType] = unset, use_tree_sitter: Union[bool, UnsetType] = unset, **kwargs
    ):
        """
        Analyzer options sent by browser-based clients. Accepted but ignored: the API always runs
        the analysis with tree-sitter enabled and rule output logged.

        :param log_output: Whether to capture the output logged by rules during execution. Ignored by this operation.
        :type log_output: bool, optional

        :param use_tree_sitter: Whether to use tree-sitter to parse the source code. Ignored by this operation.
        :type use_tree_sitter: bool, optional
        """
        if log_output is not unset:
            kwargs["log_output"] = log_output
        if use_tree_sitter is not unset:
            kwargs["use_tree_sitter"] = use_tree_sitter
        super().__init__(kwargs)
