# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class LLMObsCustomEvalConfigUser(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "email": (str,),
        }

    attribute_map = {
        "email": "email",
    }

    def __init__(self_, email: Union[str, UnsetType] = unset, **kwargs):
        """
        A Datadog user associated with a custom evaluator configuration.

        :param email: Email address of the user.
        :type email: str, optional
        """
        if email is not unset:
            kwargs["email"] = email
        super().__init__(kwargs)
