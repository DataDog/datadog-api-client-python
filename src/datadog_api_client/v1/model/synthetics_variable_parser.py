# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsVariableParser(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_global_variable_parser_type import (
            SyntheticsGlobalVariableParserType,
        )

        return {
            "type": (SyntheticsGlobalVariableParserType,),
            "value": (str,),
        }

    attribute_map = {
        "type": "type",
        "value": "value",
    }

    def __init__(self, type, *args, **kwargs):
        """
        Details of the parser to use for the global variable.

        :param type: Type of parser for a Synthetics global variable from a synthetics test.
        :type type: SyntheticsGlobalVariableParserType

        :param value: Regex or JSON path used for the parser. Not used with type ``raw``.
        :type value: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.type = type

    @classmethod
    def _from_openapi_data(cls, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsVariableParser, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.type = type
        return self
