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
    from datadog_api_client.v1_20270101.model.composite_stream_request_column20270101_width import (
        CompositeStreamRequestColumn20270101Width,
    )


class CompositeStreamRequestColumn(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.composite_stream_request_column20270101_width import (
            CompositeStreamRequestColumn20270101Width,
        )

        return {
            "alias": (str,),
            "field": (str,),
            "source": (str,),
            "width": (CompositeStreamRequestColumn20270101Width,),
        }

    attribute_map = {
        "alias": "alias",
        "field": "field",
        "source": "source",
        "width": "width",
    }

    def __init__(
        self_,
        field: str,
        width: Union[CompositeStreamRequestColumn20270101Width, float, str],
        alias: Union[str, UnsetType] = unset,
        source: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param alias: Test-only generated schema for the dashboard versioning proof of concept.
        :type alias: str, optional

        :param field: Test-only generated schema for the dashboard versioning proof of concept.
        :type field: str

        :param source: Test-only generated schema for the dashboard versioning proof of concept.
        :type source: str, optional

        :param width: Test-only generated schema for the dashboard versioning proof of concept.
        :type width: CompositeStreamRequestColumn20270101Width
        """
        if alias is not unset:
            kwargs["alias"] = alias
        if source is not unset:
            kwargs["source"] = source
        super().__init__(kwargs)

        self_.field = field
        self_.width = width
