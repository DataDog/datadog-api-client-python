# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


class RumRecoverySessionInput(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "application_id": (UUID,),
            "session_id": (UUID,),
        }

    attribute_map = {
        "application_id": "application_id",
        "session_id": "session_id",
    }

    def __init__(self_, application_id: UUID, session_id: UUID, **kwargs):
        """
        Archived session to recover.

        :param application_id: Application UUID.
        :type application_id: UUID

        :param session_id: Session UUID.
        :type session_id: UUID
        """
        super().__init__(kwargs)

        self_.application_id = application_id
        self_.session_id = session_id
