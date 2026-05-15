# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    pass


class CommitmentsTimeseriesSeries(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return ([float],)

    def __init__(self_, **kwargs):
        """
        Timeseries data as a map of series names to their corresponding value arrays.
        """
        super().__init__(kwargs)
