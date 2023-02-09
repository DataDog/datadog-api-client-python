# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.binding import Binding


class Attributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.binding import Binding

        return {
            "bindings": ([Binding],),
        }

    attribute_map = {
        "bindings": "bindings",
    }

    def __init__(self_, bindings: List[Binding], **kwargs):
        """
        Restriction policy attributes.

        :param bindings: An array of bindings.
        :type bindings: [Binding]
        """
        super().__init__(kwargs)

        self_.bindings = bindings
