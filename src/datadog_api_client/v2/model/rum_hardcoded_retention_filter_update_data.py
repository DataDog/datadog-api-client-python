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
    from datadog_api_client.v2.model.rum_hardcoded_retention_filter_update_attributes import (
        RumHardcodedRetentionFilterUpdateAttributes,
    )
    from datadog_api_client.v2.model.rum_hardcoded_retention_filter_type import RumHardcodedRetentionFilterType


class RumHardcodedRetentionFilterUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_hardcoded_retention_filter_update_attributes import (
            RumHardcodedRetentionFilterUpdateAttributes,
        )
        from datadog_api_client.v2.model.rum_hardcoded_retention_filter_type import RumHardcodedRetentionFilterType

        return {
            "attributes": (RumHardcodedRetentionFilterUpdateAttributes,),
            "id": (str,),
            "type": (RumHardcodedRetentionFilterType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: RumHardcodedRetentionFilterUpdateAttributes,
        id: str,
        type: RumHardcodedRetentionFilterType,
        **kwargs,
    ):
        """
        The hardcoded retention filter properties to update.

        :param attributes: The attributes of a hardcoded retention filter that can be updated.
            Only fields whose matching flag in ``cross_product_sampling_editability`` is ``true`` can be modified.
        :type attributes: RumHardcodedRetentionFilterUpdateAttributes

        :param id: The ID of the hardcoded retention filter. Must match the ``rf_id`` path parameter.
        :type id: str

        :param type: The resource type. The value must be ``hardcoded_retention_filters``.
        :type type: RumHardcodedRetentionFilterType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
