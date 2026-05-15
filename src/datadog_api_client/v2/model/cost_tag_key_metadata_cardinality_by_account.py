# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CostTagKeyMetadataCardinalityByAccount(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return (int,)

    def __init__(self_, **kwargs):
        """
        Number of unique tag values observed for this tag key, keyed by cloud account ID.
        """
        super().__init__(kwargs)
