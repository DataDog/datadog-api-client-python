# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
)


class SignalEntityIdentity(ModelNormal):
    def __init__(self_, **kwargs):
        """
        An identity entity related to a signal. The set of attributes is dynamic and depends on the source providing the identity.
        """
        super().__init__(kwargs)
