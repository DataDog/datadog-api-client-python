# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.synthetics_variable_parser import SyntheticsVariableParser
    from datadog_api_client.v1.model.synthetics_local_variable_parsing_options_type import (
        SyntheticsLocalVariableParsingOptionsType,
    )


class SyntheticsParsingOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_variable_parser import SyntheticsVariableParser
        from datadog_api_client.v1.model.synthetics_local_variable_parsing_options_type import (
            SyntheticsLocalVariableParsingOptionsType,
        )

        return {
            "field": (str,),
            "name": (str,),
            "parser": (SyntheticsVariableParser,),
            "secure": (bool,),
            "type": (SyntheticsLocalVariableParsingOptionsType,),
        }

    attribute_map = {
        "field": "field",
        "name": "name",
        "parser": "parser",
        "secure": "secure",
        "type": "type",
    }

    def __init__(
        self_,
        field: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        parser: Union[SyntheticsVariableParser, UnsetType] = unset,
        secure: Union[bool, UnsetType] = unset,
        type: Union[SyntheticsLocalVariableParsingOptionsType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Parsing options for variables to extract.

        :param field: When type is ``http_header`` or ``grpc_metadata`` , name of the header or metadatum to extract.
        :type field: str, optional

        :param name: Name of the variable to extract.
        :type name: str, optional

        :param parser: Details of the parser to use for the global variable.
        :type parser: SyntheticsVariableParser, optional

        :param secure: Determines whether or not the extracted value will be obfuscated.
        :type secure: bool, optional

        :param type: Property of the Synthetic Test Response to extract into a local variable.
        :type type: SyntheticsLocalVariableParsingOptionsType, optional
        """
        if field is not unset:
            kwargs["field"] = field
        if name is not unset:
            kwargs["name"] = name
        if parser is not unset:
            kwargs["parser"] = parser
        if secure is not unset:
            kwargs["secure"] = secure
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
