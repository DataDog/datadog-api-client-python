import pathlib

import click
from jinja2 import Environment, FileSystemLoader

from . import openapi
from . import formatter

PACKAGE_NAME = "datadog_api_client"


@click.command()
@click.argument(
    "specs",
    nargs=-1,
    type=click.Path(exists=True, file_okay=True, dir_okay=False, path_type=pathlib.Path),
)
@click.option(
    "-o",
    "--output",
    type=click.Path(path_type=pathlib.Path),
)
def cli(specs, output):
    """
    Generate a Python code snippet from OpenAPI specification.
    """
    env = Environment(loader=FileSystemLoader(str(pathlib.Path(__file__).parent / "templates")))

    env.filters["accept_headers"] = openapi.accept_headers
    env.filters["attribute_name"] = formatter.attribute_name
    env.filters["camel_case"] = formatter.camel_case
    env.filters["collection_format"] = openapi.collection_format
    env.filters["format_value"] = formatter.format_value
    env.filters["attribute_path"] = formatter.attribute_path
    env.filters["parameter_schema"] = openapi.parameter_schema
    env.filters["parameters"] = openapi.parameters
    env.filters["return_type"] = openapi.return_type
    env.filters["safe_snake_case"] = formatter.safe_snake_case
    env.filters["docstring"] = formatter.docstring

    env.globals["enumerate"] = enumerate
    env.globals["package"] = PACKAGE_NAME
    env.globals["get_name"] = formatter.get_name
    env.globals["get_type_for_attribute"] = openapi.get_type_for_attribute
    env.globals["get_typing_for_attribute"] = openapi.get_typing_for_attribute
    env.globals["get_types_for_attribute"] = openapi.get_types_for_attribute
    env.globals["get_type_for_parameter"] = openapi.get_type_for_parameter
    env.globals["get_references_for_model"] = openapi.get_references_for_model
    env.globals["get_oneof_references_for_model"] = openapi.get_oneof_references_for_model
    env.globals["get_oneof_parameters"] = openapi.get_oneof_parameters
    env.globals["get_type_for_items"] = openapi.get_type_for_items
    env.globals["get_api_models"] = openapi.get_api_models
    env.globals["get_enum_type"] = openapi.get_enum_type
    env.globals["get_enum_default"] = openapi.get_enum_default
    env.globals["get_oneof_types"] = openapi.get_oneof_types
    env.globals["get_oneof_models"] = openapi.get_oneof_models
    env.globals["type_to_python"] = openapi.type_to_python
    env.globals["get_default"] = openapi.get_default
    env.globals["get_type_at_path"] = openapi.get_type_at_path

    api_j2 = env.get_template("api.j2")
    apis_j2 = env.get_template("apis.j2")
    model_j2 = env.get_template("model.j2")
    models_j2 = env.get_template("models.j2")
    init_j2 = env.get_template("init.j2")
    configuration_j2 = env.get_template("configuration.j2")

    extra_files = {
        "api_client.py": env.get_template("api_client.j2"),
        "exceptions.py": env.get_template("exceptions.j2"),
        "model_utils.py": env.get_template("model_utils.j2"),
        "rest.py": env.get_template("rest.j2"),
    }

    top_package = output / PACKAGE_NAME
    top_package.mkdir(parents=True, exist_ok=True)

    for name, template in extra_files.items():
        filename = top_package / name
        with filename.open("w") as fp:
            fp.write(template.render())

    all_specs = {}
    all_apis = {}

    for spec_path in specs:
        spec = openapi.load(spec_path)
        env.globals["openapi"] = spec

        version = spec_path.parent.name
        env.globals["version"] = version

        all_specs[version] = spec

        apis = openapi.apis(spec)
        all_apis[version] = apis
        models = openapi.models(spec)

        package = top_package / version
        package.mkdir(exist_ok=True)

        for name, model in models.items():
            filename = formatter.safe_snake_case(name) + ".py"
            model_path = package / "model" / filename
            model_path.parent.mkdir(parents=True, exist_ok=True)
            with model_path.open("w") as fp:
                fp.write(model_j2.render(name=name, model=model))

        model_init_path = package / "model" / "__init__.py"
        with model_init_path.open("w") as fp:
            fp.write("")

        models_path = package / "models" / "__init__.py"
        models_path.parent.mkdir(parents=True, exist_ok=True)
        with models_path.open("w") as fp:
            fp.write(models_j2.render(models=sorted(models)))

        tags_by_name = {tag["name"]: tag for tag in spec["tags"]}

        for name, operations in apis.items():
            filename = formatter.safe_snake_case(name) + "_api.py"
            api_path = package / "api" / filename
            api_path.parent.mkdir(parents=True, exist_ok=True)
            with api_path.open("w") as fp:
                fp.write(api_j2.render(name=name, operations=operations, description=tags_by_name[name]["description"]))

        api_init_path = package / "api" / "__init__.py"
        with api_init_path.open("w") as fp:
            fp.write("")

        apis_path = package / "apis" / "__init__.py"
        apis_path.parent.mkdir(parents=True, exist_ok=True)
        with apis_path.open("w") as fp:
            fp.write(apis_j2.render(apis=sorted(apis)))

        init_path = package / "__init__.py"
        with init_path.open("w") as fp:
            fp.write(init_j2.render())

    filename = top_package / "configuration.py"
    with filename.open("w") as fp:
        fp.write(configuration_j2.render(specs=all_specs, apis=all_apis))
