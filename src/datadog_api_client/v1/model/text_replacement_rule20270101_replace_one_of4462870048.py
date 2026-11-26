# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class TextReplacementRule20270101ReplaceOneOf4462870048(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "type": (TextReplacementRuleReplaceAnyOfAnyOfItemType4452739616,),
            "_with": (str,),
        }

    attribute_map = {
        "type": "type",
        "_with": "with",
    }

    def __init__(self_, type: TextReplacementRuleReplaceAnyOfAnyOfItemType4452739616, _with: str, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: TextReplacementRuleReplaceAnyOfAnyOfItemType4452739616

        :param _with: Test-only generated schema for the dashboard versioning proof of concept.
        :type _with: str
        """
        super().__init__(kwargs)

        self_.type = type
        self_._with = _with
