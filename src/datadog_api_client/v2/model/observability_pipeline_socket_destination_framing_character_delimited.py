# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_socket_destination_framing_character_delimited_method import (
        ObservabilityPipelineSocketDestinationFramingCharacterDelimitedMethod,
    )


class ObservabilityPipelineSocketDestinationFramingCharacterDelimited(ModelNormal):
    validations = {
        "delimiter": {
            "max_length": 1,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_socket_destination_framing_character_delimited_method import (
            ObservabilityPipelineSocketDestinationFramingCharacterDelimitedMethod,
        )

        return {
            "delimiter": (str,),
            "method": (ObservabilityPipelineSocketDestinationFramingCharacterDelimitedMethod,),
        }

    attribute_map = {
        "delimiter": "delimiter",
        "method": "method",
    }

    def __init__(
        self_, delimiter: str, method: ObservabilityPipelineSocketDestinationFramingCharacterDelimitedMethod, **kwargs
    ):
        """
        Each log event is separated using the specified delimiter character.

        :param delimiter: A single ASCII character used as a delimiter.
        :type delimiter: str

        :param method: The definition of ``ObservabilityPipelineSocketDestinationFramingCharacterDelimitedMethod`` object.
        :type method: ObservabilityPipelineSocketDestinationFramingCharacterDelimitedMethod
        """
        super().__init__(kwargs)

        self_.delimiter = delimiter
        self_.method = method
