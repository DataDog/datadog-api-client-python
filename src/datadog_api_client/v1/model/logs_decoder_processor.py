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
    from datadog_api_client.v1.model.logs_decoder_processor_binary_to_text_encoding import (
        LogsDecoderProcessorBinaryToTextEncoding,
    )
    from datadog_api_client.v1.model.logs_decoder_processor_input_representation import (
        LogsDecoderProcessorInputRepresentation,
    )
    from datadog_api_client.v1.model.logs_decoder_processor_type import LogsDecoderProcessorType


class LogsDecoderProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.logs_decoder_processor_binary_to_text_encoding import (
            LogsDecoderProcessorBinaryToTextEncoding,
        )
        from datadog_api_client.v1.model.logs_decoder_processor_input_representation import (
            LogsDecoderProcessorInputRepresentation,
        )
        from datadog_api_client.v1.model.logs_decoder_processor_type import LogsDecoderProcessorType

        return {
            "binary_to_text_encoding": (LogsDecoderProcessorBinaryToTextEncoding,),
            "input_representation": (LogsDecoderProcessorInputRepresentation,),
            "is_enabled": (bool,),
            "name": (str,),
            "source": (str,),
            "target": (str,),
            "type": (LogsDecoderProcessorType,),
        }

    attribute_map = {
        "binary_to_text_encoding": "binary_to_text_encoding",
        "input_representation": "input_representation",
        "is_enabled": "is_enabled",
        "name": "name",
        "source": "source",
        "target": "target",
        "type": "type",
    }

    def __init__(
        self_,
        binary_to_text_encoding: LogsDecoderProcessorBinaryToTextEncoding,
        input_representation: LogsDecoderProcessorInputRepresentation,
        source: str,
        target: str,
        type: LogsDecoderProcessorType,
        is_enabled: Union[bool, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The decoder processor decodes any source attribute containing a
        base64/base16-encoded UTF-8/ASCII string back to its original value, storing the
        result in a target attribute.

        :param binary_to_text_encoding: The encoding used to represent the binary data.
        :type binary_to_text_encoding: LogsDecoderProcessorBinaryToTextEncoding

        :param input_representation: The original representation of input string.
        :type input_representation: LogsDecoderProcessorInputRepresentation

        :param is_enabled: Whether the processor is enabled.
        :type is_enabled: bool, optional

        :param name: Name of the processor.
        :type name: str, optional

        :param source: Name of the log attribute with the encoded data.
        :type source: str

        :param target: Name of the log attribute that contains the decoded data.
        :type target: str

        :param type: Type of logs decoder processor.
        :type type: LogsDecoderProcessorType
        """
        if is_enabled is not unset:
            kwargs["is_enabled"] = is_enabled
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.binary_to_text_encoding = binary_to_text_encoding
        self_.input_representation = input_representation
        self_.source = source
        self_.target = target
        self_.type = type
