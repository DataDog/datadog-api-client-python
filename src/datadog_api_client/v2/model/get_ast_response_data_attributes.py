# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    UUID,
)


class GetAstResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "ast": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
        }

    attribute_map = {
        "ast": "ast",
    }

    def __init__(self_, ast: Dict[str, Any], **kwargs):
        """
        The attributes of the get-AST response, containing the parsed abstract syntax tree.

        :param ast: The parsed abstract syntax tree as a JSON object.
        :type ast: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}
        """
        super().__init__(kwargs)

        self_.ast = ast
