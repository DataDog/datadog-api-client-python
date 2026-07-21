# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class LLMObsDeletedPromptDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "deleted_at": (datetime,),
            "prompt_id": (str,),
        }

    attribute_map = {
        "deleted_at": "deleted_at",
        "prompt_id": "prompt_id",
    }

    def __init__(self_, deleted_at: datetime, prompt_id: str, **kwargs):
        """
        Attributes confirming that an LLM Observability prompt was deleted.

        :param deleted_at: Timestamp when the prompt was deleted.
        :type deleted_at: datetime

        :param prompt_id: Customer-provided identifier of the deleted prompt.
        :type prompt_id: str
        """
        super().__init__(kwargs)

        self_.deleted_at = deleted_at
        self_.prompt_id = prompt_id
