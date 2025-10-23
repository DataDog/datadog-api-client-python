"""
Create a pipeline with Schema Processor and preserve_source false returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi
from datadog_api_client.v1.model.logs_filter import LogsFilter
from datadog_api_client.v1.model.logs_pipeline import LogsPipeline
from datadog_api_client.v1.model.logs_schema_category_mapper import LogsSchemaCategoryMapper
from datadog_api_client.v1.model.logs_schema_category_mapper_category import LogsSchemaCategoryMapperCategory
from datadog_api_client.v1.model.logs_schema_category_mapper_fallback import LogsSchemaCategoryMapperFallback
from datadog_api_client.v1.model.logs_schema_category_mapper_targets import LogsSchemaCategoryMapperTargets
from datadog_api_client.v1.model.logs_schema_category_mapper_type import LogsSchemaCategoryMapperType
from datadog_api_client.v1.model.logs_schema_data import LogsSchemaData
from datadog_api_client.v1.model.logs_schema_processor import LogsSchemaProcessor
from datadog_api_client.v1.model.logs_schema_processor_type import LogsSchemaProcessorType
from datadog_api_client.v1.model.logs_schema_remapper import LogsSchemaRemapper
from datadog_api_client.v1.model.logs_schema_remapper_type import LogsSchemaRemapperType

body = LogsPipeline(
    filter=LogsFilter(
        query="source:python",
    ),
    name="testSchemaProcessor",
    processors=[
        LogsSchemaProcessor(
            type=LogsSchemaProcessorType.SCHEMA_PROCESSOR,
            is_enabled=True,
            name="Apply OCSF schema for 3001",
            schema=LogsSchemaData(
                schema_type="ocsf",
                version="1.5.0",
                class_uid=3001,
                class_name="Account Change",
                profiles=[
                    "cloud",
                    "datetime",
                ],
            ),
            mappers=[
                LogsSchemaCategoryMapper(
                    type=LogsSchemaCategoryMapperType.SCHEMA_CATEGORY_MAPPER,
                    name="activity_id and activity_name",
                    categories=[
                        LogsSchemaCategoryMapperCategory(
                            filter=LogsFilter(
                                query="@eventName:(*Create*)",
                            ),
                            name="Create",
                            id=1,
                        ),
                        LogsSchemaCategoryMapperCategory(
                            filter=LogsFilter(
                                query="@eventName:(ChangePassword OR PasswordUpdated)",
                            ),
                            name="Password Change",
                            id=3,
                        ),
                        LogsSchemaCategoryMapperCategory(
                            filter=LogsFilter(
                                query="@eventName:(*Attach*)",
                            ),
                            name="Attach Policy",
                            id=7,
                        ),
                        LogsSchemaCategoryMapperCategory(
                            filter=LogsFilter(
                                query="@eventName:(*Detach* OR *Remove*)",
                            ),
                            name="Detach Policy",
                            id=8,
                        ),
                        LogsSchemaCategoryMapperCategory(
                            filter=LogsFilter(
                                query="@eventName:(*Delete*)",
                            ),
                            name="Delete",
                            id=6,
                        ),
                        LogsSchemaCategoryMapperCategory(
                            filter=LogsFilter(
                                query="@eventName:*",
                            ),
                            name="Other",
                            id=99,
                        ),
                    ],
                    targets=LogsSchemaCategoryMapperTargets(
                        name="ocsf.activity_name",
                        id="ocsf.activity_id",
                    ),
                    fallback=LogsSchemaCategoryMapperFallback(
                        values={
                            "ocsf.activity_id": "99",
                            "ocsf.activity_name": "Other",
                        },
                        sources={
                            "ocsf.activity_name": [
                                "eventName",
                            ],
                        },
                    ),
                ),
                LogsSchemaCategoryMapper(
                    type=LogsSchemaCategoryMapperType.SCHEMA_CATEGORY_MAPPER,
                    name="status",
                    categories=[
                        LogsSchemaCategoryMapperCategory(
                            filter=LogsFilter(
                                query="-@errorCode:*",
                            ),
                            id=1,
                            name="Success",
                        ),
                        LogsSchemaCategoryMapperCategory(
                            filter=LogsFilter(
                                query="@errorCode:*",
                            ),
                            id=2,
                            name="Failure",
                        ),
                    ],
                    targets=LogsSchemaCategoryMapperTargets(
                        id="ocsf.status_id",
                        name="ocsf.status",
                    ),
                ),
                LogsSchemaCategoryMapper(
                    type=LogsSchemaCategoryMapperType.SCHEMA_CATEGORY_MAPPER,
                    name="Set default severity",
                    categories=[
                        LogsSchemaCategoryMapperCategory(
                            filter=LogsFilter(
                                query="@eventName:*",
                            ),
                            name="Informational",
                            id=1,
                        ),
                    ],
                    targets=LogsSchemaCategoryMapperTargets(
                        name="ocsf.severity",
                        id="ocsf.severity_id",
                    ),
                ),
                LogsSchemaRemapper(
                    type=LogsSchemaRemapperType.SCHEMA_REMAPPER,
                    name="Map userIdentity to ocsf.user.uid",
                    sources=[
                        "userIdentity.principalId",
                        "responseElements.role.roleId",
                        "responseElements.user.userId",
                    ],
                    target="ocsf.user.uid",
                    preserve_source=False,
                ),
                LogsSchemaRemapper(
                    type=LogsSchemaRemapperType.SCHEMA_REMAPPER,
                    name="Map userName to ocsf.user.name",
                    sources=[
                        "requestParameters.userName",
                        "responseElements.role.roleName",
                        "requestParameters.roleName",
                        "responseElements.user.userName",
                    ],
                    target="ocsf.user.name",
                    preserve_source=False,
                ),
                LogsSchemaRemapper(
                    type=LogsSchemaRemapperType.SCHEMA_REMAPPER,
                    name="Map api to ocsf.api",
                    sources=[
                        "api",
                    ],
                    target="ocsf.api",
                    preserve_source=False,
                ),
                LogsSchemaRemapper(
                    type=LogsSchemaRemapperType.SCHEMA_REMAPPER,
                    name="Map user to ocsf.user",
                    sources=[
                        "user",
                    ],
                    target="ocsf.user",
                    preserve_source=False,
                ),
                LogsSchemaRemapper(
                    type=LogsSchemaRemapperType.SCHEMA_REMAPPER,
                    name="Map actor to ocsf.actor",
                    sources=[
                        "actor",
                    ],
                    target="ocsf.actor",
                    preserve_source=False,
                ),
                LogsSchemaRemapper(
                    type=LogsSchemaRemapperType.SCHEMA_REMAPPER,
                    name="Map cloud to ocsf.cloud",
                    sources=[
                        "cloud",
                    ],
                    target="ocsf.cloud",
                    preserve_source=False,
                ),
                LogsSchemaRemapper(
                    type=LogsSchemaRemapperType.SCHEMA_REMAPPER,
                    name="Map http_request to ocsf.http_request",
                    sources=[
                        "http_request",
                    ],
                    target="ocsf.http_request",
                    preserve_source=False,
                ),
                LogsSchemaRemapper(
                    type=LogsSchemaRemapperType.SCHEMA_REMAPPER,
                    name="Map metadata to ocsf.metadata",
                    sources=[
                        "metadata",
                    ],
                    target="ocsf.metadata",
                    preserve_source=False,
                ),
                LogsSchemaRemapper(
                    type=LogsSchemaRemapperType.SCHEMA_REMAPPER,
                    name="Map time to ocsf.time",
                    sources=[
                        "time",
                    ],
                    target="ocsf.time",
                    preserve_source=False,
                ),
                LogsSchemaRemapper(
                    type=LogsSchemaRemapperType.SCHEMA_REMAPPER,
                    name="Map src_endpoint to ocsf.src_endpoint",
                    sources=[
                        "src_endpoint",
                    ],
                    target="ocsf.src_endpoint",
                    preserve_source=False,
                ),
                LogsSchemaRemapper(
                    type=LogsSchemaRemapperType.SCHEMA_REMAPPER,
                    name="Map severity to ocsf.severity",
                    sources=[
                        "severity",
                    ],
                    target="ocsf.severity",
                    preserve_source=False,
                ),
                LogsSchemaRemapper(
                    type=LogsSchemaRemapperType.SCHEMA_REMAPPER,
                    name="Map severity_id to ocsf.severity_id",
                    sources=[
                        "severity_id",
                    ],
                    target="ocsf.severity_id",
                    preserve_source=False,
                ),
            ],
        ),
    ],
    tags=[],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsPipelinesApi(api_client)
    response = api_instance.create_logs_pipeline(body=body)

    print(response)
