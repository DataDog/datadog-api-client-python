# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.logs_user_agent_parser_type import LogsUserAgentParserType

    globals()["LogsUserAgentParserType"] = LogsUserAgentParserType


class LogsUserAgentParser(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "is_enabled": (bool,),
            "is_encoded": (bool,),
            "name": (str,),
            "sources": ([str],),
            "target": (str,),
            "type": (LogsUserAgentParserType,),
        }

    attribute_map = {
        "is_enabled": "is_enabled",
        "is_encoded": "is_encoded",
        "name": "name",
        "sources": "sources",
        "target": "target",
        "type": "type",
    }

    read_only_vars = {}

    def __init__(self, type, *args, **kwargs):
        """
        The User-Agent parser takes a User-Agent attribute and extracts the OS, browser, device, and other user data.
        It recognizes major bots like the Google Bot, Yahoo Slurp, and Bing.

        :param is_enabled: Whether or not the processor is enabled.
        :type is_enabled: bool, optional

        :param is_encoded: Define if the source attribute is URL encoded or not.
        :type is_encoded: bool, optional

        :param name: Name of the processor.
        :type name: str, optional

        :param sources: Array of source attributes.
        :type sources: [str]

        :param target: Name of the parent attribute that contains all the extracted details from the `sources`.
        :type target: str

        :param type: Type of logs User-Agent parser.
        :type type: LogsUserAgentParserType
        """
        super().__init__(kwargs)
        sources = kwargs.get("sources", ["http.useragent"])
        target = kwargs.get("target", "http.useragent_details")

        self._check_pos_args(args)

        self.sources = sources
        self.target = target
        self.type = type

    @classmethod
    def _from_openapi_data(cls, type, *args, **kwargs):
        """Helper creating a new instance from a response."""
        sources = kwargs.get("sources", ["http.useragent"])
        target = kwargs.get("target", "http.useragent_details")

        self = super(LogsUserAgentParser, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.sources = sources
        self.target = target
        self.type = type
        return self
