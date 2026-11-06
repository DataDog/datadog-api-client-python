# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class RumRecoveryCreateAttributes(ModelComposed):
    def __init__(self, **kwargs):
        """
        Targeted recovery (the default) or query-based batch recovery.

        :param request_type: Targeted recovery. Omitted request_type defaults to sessions.
        :type request_type: RumRecoverySessionsRequestType, optional

        :param sessions: Sessions to recover.
        :type sessions: [RumRecoverySessionInput]

        :param estimated_count: Optional client estimate. Creation validates and stores a fresh server estimate instead of this value.
        :type estimated_count: int, optional

        :param _from: Start of the range in Unix milliseconds. Must be positive and earlier than to.
        :type _from: int

        :param query: RUM search query. Not blank, at most 4096 bytes for batch creation and count.
        :type query: str

        :param to: End of the range in Unix milliseconds.
        :type to: int
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.rum_recovery_sessions_create_attributes import (
            RumRecoverySessionsCreateAttributes,
        )
        from datadog_api_client.v2.model.rum_recovery_batch_create_attributes import RumRecoveryBatchCreateAttributes

        return {
            "oneOf": [
                RumRecoverySessionsCreateAttributes,
                RumRecoveryBatchCreateAttributes,
            ],
        }
