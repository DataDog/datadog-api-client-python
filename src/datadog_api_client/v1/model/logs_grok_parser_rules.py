# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsGrokParserRules(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "match_rules": (str,),
            "support_rules": (str,),
        }

    attribute_map = {
        "match_rules": "match_rules",
        "support_rules": "support_rules",
    }

    def __init__(self, match_rules, *args, **kwargs):
        """
        Set of rules for the grok parser.

        :param match_rules: List of match rules for the grok parser, separated by a new line.
        :type match_rules: str

        :param support_rules: List of support rules for the grok parser, separated by a new line.
        :type support_rules: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.match_rules = match_rules

    @classmethod
    def _from_openapi_data(cls, match_rules, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsGrokParserRules, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.match_rules = match_rules
        return self
