# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    pass


class WidgetAnnotationsMap(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return ([UUID],)

    def __init__(self_, **kwargs):
        """
        Map from widget ID to the list of annotation IDs displayed on that widget.
        """
        super().__init__(kwargs)
