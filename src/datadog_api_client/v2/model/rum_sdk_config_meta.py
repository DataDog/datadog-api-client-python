# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class RumSdkConfigMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "updated_at": (datetime,),
            "updated_by": (str,),
        }

    attribute_map = {
        "updated_at": "updated_at",
        "updated_by": "updated_by",
    }

    def __init__(self_, updated_at: datetime, updated_by: str, **kwargs):
        """
        Metadata associated with a RUM SDK configuration.

        :param updated_at: The timestamp of the last update to this configuration.
        :type updated_at: datetime

        :param updated_by: The handle of the user who last updated this configuration.
        :type updated_by: str
        """
        super().__init__(kwargs)

        self_.updated_at = updated_at
        self_.updated_by = updated_by
