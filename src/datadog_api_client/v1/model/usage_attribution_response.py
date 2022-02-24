# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.usage_attribution_metadata import UsageAttributionMetadata
    from datadog_api_client.v1.model.usage_attribution_body import UsageAttributionBody

    globals()["UsageAttributionMetadata"] = UsageAttributionMetadata
    globals()["UsageAttributionBody"] = UsageAttributionBody


class UsageAttributionResponse(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "metadata": (UsageAttributionMetadata,),
            "usage": ([UsageAttributionBody],),
        }

    attribute_map = {
        "metadata": "metadata",
        "usage": "usage",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Response containing the Usage Summary by tag(s).

        :param metadata: The object containing document metadata.
        :type metadata: UsageAttributionMetadata, optional

        :param usage: Get Usage Summary by tag(s).
        :type usage: [UsageAttributionBody], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageAttributionResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
