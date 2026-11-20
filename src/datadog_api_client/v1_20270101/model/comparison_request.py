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
    from datadog_api_client.v1_20270101.model.change_directionality import ChangeDirectionality
    from datadog_api_client.v1_20270101.model.change_duration import ChangeDuration
    from datadog_api_client.v1_20270101.model.change_layout import ChangeLayout
    from datadog_api_client.v1_20270101.model.change_type import ChangeType
    from datadog_api_client.v1_20270101.model.change_duration20270101_one_of import ChangeDuration20270101OneOf
    from datadog_api_client.v1_20270101.model.change_duration20270101_one_of4454627136 import (
        ChangeDuration20270101OneOf4454627136,
    )


class ComparisonRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.change_directionality import ChangeDirectionality
        from datadog_api_client.v1_20270101.model.change_duration import ChangeDuration
        from datadog_api_client.v1_20270101.model.change_layout import ChangeLayout
        from datadog_api_client.v1_20270101.model.change_type import ChangeType

        return {
            "directionality": (ChangeDirectionality,),
            "duration": (ChangeDuration,),
            "layout": (ChangeLayout,),
            "type": (ChangeType,),
        }

    attribute_map = {
        "directionality": "directionality",
        "duration": "duration",
        "layout": "layout",
        "type": "type",
    }

    def __init__(
        self_,
        duration: Union[ChangeDuration, ChangeDuration20270101OneOf, ChangeDuration20270101OneOf4454627136],
        directionality: Union[ChangeDirectionality, UnsetType] = unset,
        layout: Union[ChangeLayout, UnsetType] = unset,
        type: Union[ChangeType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param directionality: Test-only generated schema for the dashboard versioning proof of concept.
        :type directionality: ChangeDirectionality, optional

        :param duration: Test-only generated schema for the dashboard versioning proof of concept.
        :type duration: ChangeDuration

        :param layout: Test-only generated schema for the dashboard versioning proof of concept.
        :type layout: ChangeLayout, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: ChangeType, optional
        """
        if directionality is not unset:
            kwargs["directionality"] = directionality
        if layout is not unset:
            kwargs["layout"] = layout
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.duration = duration
