# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RulesetItemMetadata(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return (str,)

    _nullable = True

    def __init__(self_, **kwargs):
        """
        The ``items`` ``metadata``.
        """
        super().__init__(kwargs)
