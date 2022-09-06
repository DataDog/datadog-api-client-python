# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RUMAggregationBucketsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_bucket_response import RUMBucketResponse

        return {
            "buckets": ([RUMBucketResponse],),
        }

    attribute_map = {
        "buckets": "buckets",
    }

    def __init__(self_, *args, **kwargs):
        """
        The query results.

        :param buckets: The list of matching buckets, one item per bucket.
        :type buckets: [RUMBucketResponse], optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
