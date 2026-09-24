# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
)


class LLMObsPromptConfig(ModelNormal):
    def __init__(self_, **kwargs):
        """
        Versioned prompt configuration is in Preview. To request access, contact `Datadog Support <https://www.datadoghq.com/support/>`_ or your Customer Success Manager. Customer-owned configuration delivered with a prompt version. Datadog stores and returns the object without interpolating it, validating provider-specific keys, or applying it to model calls. Do not include secrets.
        """
        super().__init__(kwargs)
