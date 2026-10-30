# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UsageQuotaRequestScope(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return (str,)

    def __init__(self_, **kwargs):
        """
        A namespace-specific key and value identifying what the quota applies to within an organization. See the endpoint description for the supported scope keys, values, and validation rules.
        """
        super().__init__(kwargs)
