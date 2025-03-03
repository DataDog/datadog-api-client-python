# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
)


class ActionQuerySpecInput(ModelNormal):
    def __init__(self_, **kwargs):
        """
        The inputs to the action query. See the `Actions Catalog <https://docs.datadoghq.com/actions/actions_catalog/>`_ for more detail on each action and its inputs.
        """
        super().__init__(kwargs)
