# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
)


class EntityContextRevisionAttributes(ModelNormal):
    def __init__(self_, **kwargs):
        """
        The set of attributes recorded for the entity at this revision. The keys depend on the kind of entity.
        """
        super().__init__(kwargs)
