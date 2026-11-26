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
    from datadog_api_client.v1_20270101.model.logs_stream_request_columns_items20270101_width import (
        LogsStreamRequestColumnsItems20270101Width,
    )


class LogsStreamRequestColumnsItems(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.logs_stream_request_columns_items20270101_width import (
            LogsStreamRequestColumnsItems20270101Width,
        )

        return {
            "alias": (str,),
            "field": (str,),
            "width": (LogsStreamRequestColumnsItems20270101Width,),
        }

    attribute_map = {
        "alias": "alias",
        "field": "field",
        "width": "width",
    }

    def __init__(
        self_,
        field: str,
        width: Union[LogsStreamRequestColumnsItems20270101Width, float, str],
        alias: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param alias: Test-only generated schema for the dashboard versioning proof of concept.
        :type alias: str, optional

        :param field: Test-only generated schema for the dashboard versioning proof of concept.
        :type field: str

        :param width: Test-only generated schema for the dashboard versioning proof of concept.
        :type width: LogsStreamRequestColumnsItems20270101Width
        """
        if alias is not unset:
            kwargs["alias"] = alias
        super().__init__(kwargs)

        self_.field = field
        self_.width = width
