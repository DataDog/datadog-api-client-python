# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


def lazy_import():
    from datadog_api_client.v1.model.logs_url_parser_type import LogsURLParserType

    globals()["LogsURLParserType"] = LogsURLParserType


class LogsURLParser(ModelNormal):
    @cached_property
    def openapi_types(_):
        lazy_import()
        return {
            "is_enabled": (bool,),
            "name": (str,),
            "normalize_ending_slashes": (bool, none_type),
            "sources": ([str],),
            "target": (str,),
            "type": (LogsURLParserType,),
        }

    attribute_map = {
        "is_enabled": "is_enabled",
        "name": "name",
        "normalize_ending_slashes": "normalize_ending_slashes",
        "sources": "sources",
        "target": "target",
        "type": "type",
    }

    def __init__(self, type, *args, **kwargs):
        """
        This processor extracts query parameters and other important parameters from a URL.

        :param is_enabled: Whether or not the processor is enabled.
        :type is_enabled: bool, optional

        :param name: Name of the processor.
        :type name: str, optional

        :param normalize_ending_slashes: Normalize the ending slashes or not.
        :type normalize_ending_slashes: bool, none_type, optional

        :param sources: Array of source attributes.
        :type sources: [str]

        :param target: Name of the parent attribute that contains all the extracted details from the `sources`.
        :type target: str

        :param type: Type of logs URL parser.
        :type type: LogsURLParserType
        """
        super().__init__(kwargs)
        sources = kwargs.get("sources", ["http.url"])
        target = kwargs.get("target", "http.url_details")

        self._check_pos_args(args)

        self.sources = sources
        self.target = target
        self.type = type

    @classmethod
    def _from_openapi_data(cls, type, *args, **kwargs):
        """Helper creating a new instance from a response."""
        sources = kwargs.get("sources", ["http.url"])
        target = kwargs.get("target", "http.url_details")

        self = super(LogsURLParser, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.sources = sources
        self.target = target
        self.type = type
        return self
