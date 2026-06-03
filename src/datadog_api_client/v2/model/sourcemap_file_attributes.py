# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    UUID,
)


class SourcemapFileAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "file": (str,),
            "mappings": (str,),
            "minified_line_lengths": ([int],),
            "names": ([bool, date, datetime, dict, float, int, list, str, UUID, none_type],),
            "source_root": (str,),
            "sources": ([str],),
            "sources_content": ([str],),
            "version": (int,),
        }

    attribute_map = {
        "file": "file",
        "mappings": "mappings",
        "minified_line_lengths": "minifiedLineLengths",
        "names": "names",
        "source_root": "sourceRoot",
        "sources": "sources",
        "sources_content": "sourcesContent",
        "version": "version",
    }

    def __init__(
        self_,
        file: str,
        mappings: str,
        minified_line_lengths: List[int],
        names: List[Any],
        source_root: str,
        sources: List[str],
        sources_content: List[str],
        version: int,
        **kwargs,
    ):
        """
        Attributes of a JavaScript source map file.

        :param file: The name of the minified JavaScript file.
        :type file: str

        :param mappings: The Base64 VLQ encoded string that maps positions in the minified
            file to positions in the original source files.
        :type mappings: str

        :param minified_line_lengths: List of character counts for each line in the minified file.
        :type minified_line_lengths: [int]

        :param names: List of symbol names referenced in the mappings.
        :type names: [bool, date, datetime, dict, float, int, list, str, UUID, none_type]

        :param source_root: The root path prepended to source file paths.
        :type source_root: str

        :param sources: List of original source file paths.
        :type sources: [str]

        :param sources_content: List of original source file contents corresponding to the paths in ``sources``.
        :type sources_content: [str]

        :param version: The version of the source map format (typically 3).
        :type version: int
        """
        super().__init__(kwargs)

        self_.file = file
        self_.mappings = mappings
        self_.minified_line_lengths = minified_line_lengths
        self_.names = names
        self_.source_root = source_root
        self_.sources = sources
        self_.sources_content = sources_content
        self_.version = version
