# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.error_errors_items import ErrorErrorsItems


class Error(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.error_errors_items import ErrorErrorsItems

        return {
            "errors": ([ErrorErrorsItems, none_type],),
        }

    attribute_map = {
        "errors": "errors",
    }

    def __init__(self_, errors: Union[List[ErrorErrorsItems], UnsetType] = unset, **kwargs):
        """
        The definition of ``Error`` object.

        :param errors: The ``Error`` ``errors``.
        :type errors: [ErrorErrorsItems, none_type], optional
        """
        if errors is not unset:
            kwargs["errors"] = errors
        super().__init__(kwargs)
