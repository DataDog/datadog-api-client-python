# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ObservabilityPipelineEnrichmentTableFieldSecretLookup(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "secret": (str,),
        }

    attribute_map = {
        "secret": "secret",
    }

    def __init__(self_, secret: str, **kwargs):
        """
        Looks up a value stored as a pipeline secret.

        :param secret: The name of the secret containing the lookup key value.
        :type secret: str
        """
        super().__init__(kwargs)

        self_.secret = secret
