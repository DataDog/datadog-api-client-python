# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsPromptVersionLabel(ModelSimple):
    """
    A label attached to an LLM Observability prompt version.

    :param value: Must be one of ["production", "development"].
    :type value: str
    """

    allowed_values = {
        "production",
        "development",
    }
    PRODUCTION: ClassVar["LLMObsPromptVersionLabel"]
    DEVELOPMENT: ClassVar["LLMObsPromptVersionLabel"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsPromptVersionLabel.PRODUCTION = LLMObsPromptVersionLabel("production")
LLMObsPromptVersionLabel.DEVELOPMENT = LLMObsPromptVersionLabel("development")
