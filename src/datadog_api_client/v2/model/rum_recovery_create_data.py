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
    from datadog_api_client.v2.model.rum_recovery_create_attributes import RumRecoveryCreateAttributes
    from datadog_api_client.v2.model.rum_recovery_sessions_create_attributes import RumRecoverySessionsCreateAttributes
    from datadog_api_client.v2.model.rum_recovery_batch_create_attributes import RumRecoveryBatchCreateAttributes


class RumRecoveryCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_recovery_create_attributes import RumRecoveryCreateAttributes

        return {
            "attributes": (RumRecoveryCreateAttributes,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[
            RumRecoveryCreateAttributes, RumRecoverySessionsCreateAttributes, RumRecoveryBatchCreateAttributes
        ],
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        JSON:API resource.

        :param attributes: Targeted recovery (the default) or query-based batch recovery.
        :type attributes: RumRecoveryCreateAttributes

        :param type: JSON:API resource type.
        :type type: str, optional
        """
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.attributes = attributes
