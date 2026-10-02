# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


class ExperimentsSavedFilterCondition(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "saved_filter_id": (UUID,),
        }

    attribute_map = {
        "saved_filter_id": "saved_filter_id",
    }

    def __init__(self_, saved_filter_id: UUID, **kwargs):
        """
        A condition that uses a saved filter. Inline fields must be omitted or null.

        :param saved_filter_id: Saved-filter UUID.
        :type saved_filter_id: UUID
        """
        super().__init__(kwargs)

        self_.saved_filter_id = saved_filter_id
