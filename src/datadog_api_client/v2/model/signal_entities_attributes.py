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
    from datadog_api_client.v2.model.signal_entity_identity import SignalEntityIdentity


class SignalEntitiesAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.signal_entity_identity import SignalEntityIdentity

        return {
            "identities": ([SignalEntityIdentity],),
        }

    attribute_map = {
        "identities": "identities",
    }

    def __init__(self_, identities: List[SignalEntityIdentity], **kwargs):
        """
        Attributes containing the entities related to the signal.

        :param identities: The identity entities related to the signal. Each item is a free-form object describing an identity (for example, a user or principal).
        :type identities: [SignalEntityIdentity]
        """
        super().__init__(kwargs)

        self_.identities = identities
