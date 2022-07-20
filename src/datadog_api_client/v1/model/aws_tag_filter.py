# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AWSTagFilter(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.aws_namespace import AWSNamespace

        return {
            "namespace": (AWSNamespace,),
            "tag_filter_str": (str,),
        }

    attribute_map = {
        "namespace": "namespace",
        "tag_filter_str": "tag_filter_str",
    }

    def __init__(self, *args, **kwargs):
        """
        A tag filter.

        :param namespace: The namespace associated with the tag filter entry.
        :type namespace: AWSNamespace, optional

        :param tag_filter_str: The tag filter string.
        :type tag_filter_str: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(AWSTagFilter, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
