# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class BudgetValidationResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "errors": ([str],),
            "valid": (bool,),
        }

    attribute_map = {
        "errors": "errors",
        "valid": "valid",
    }

    def __init__(self_, errors: Union[List[str], UnsetType] = unset, valid: Union[bool, UnsetType] = unset, **kwargs):
        """


        :param errors:
        :type errors: [str], optional

        :param valid:
        :type valid: bool, optional
        """
        if errors is not unset:
            kwargs["errors"] = errors
        if valid is not unset:
            kwargs["valid"] = valid
        super().__init__(kwargs)
